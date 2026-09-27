# -*- coding: utf-8 -*-
"""
Gera o DVP em .docx a partir do markdown, usando DVP_Template.docx da UPF como base.

    python docs/build_docx.py

O que faz:
  1. prepara o markdown (remove sumario manual e blocos de codigo Mermaid);
  2. converte com pandoc usando o template como --reference-doc, o que herda
     estilos (Ttulo1..6), numeracao, margens, cabecalho e rodape da UPF;
  3. corrige o que o pandoc nao acerta sozinho:
       - transplanta a capa real do template, com os placeholders preenchidos;
       - move o campo TOC para depois do historico de alteracoes;
       - aplica o estilo de tabela do template (Tabelacomgrade);
       - preenche os placeholders do cabecalho (projeto, versao, data);
  4. reempacota o .docx.

Depois de gerar, abra no Word e tecle Ctrl+A / F9 para atualizar o sumario
(ou rode docs/update_toc.ps1).
"""
import os, re, shutil, subprocess, sys, tempfile, zipfile
import xml.etree.ElementTree as ET

RAIZ     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD       = os.path.join(RAIZ, "docs", "DVP_Agiliza_Delivery_latest_version.md")
TEMPLATE = os.path.join(RAIZ, "docs", "old_versions", "DVP_Template.docx")
SAIDA    = os.path.join(RAIZ, "docs", "DVP_Agiliza_Delivery_v2.1.docx")

PROJETO = "Projeto Agiliza Delivery Documento de Visão do Produto - DVP"
VERSAO  = "Versão: 2.1"
DATA    = "16/09/2026"
ALUNO   = "Eduardo dos Santos de Camargo"
TITULO  = "AGILIZA DELIVERY"
ANO     = "2026"

PB = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def prepara_markdown(destino):
    s = open(MD, encoding="utf-8").read()
    # o campo TOC do Word substitui o sumario escrito a mao
    s = re.sub(r"\n## Sumário\n.*?\n---\n", "\n", s, flags=re.S, count=1)
    # o fonte Mermaid nao vai para o Word (o PNG ja esta no documento)
    s = re.sub(r"<details>\s*<summary>.*?</summary>\s*```mermaid.*?```\s*</details>\s*",
               "", s, flags=re.S)
    # no template da UPF esse titulo e texto Normal em negrito, nao um Titulo,
    # por isso nao deve aparecer no sumario
    s = s.replace("## Histórico de alterações do documento",
                  "**Histórico de alterações do documento**", 1)

    open(destino, "w", encoding="utf-8").write(s)
    return s


def texto_do_paragrafo(p):
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))


def reescreve_paragrafo(p, novo):
    """troca todos os runs de texto do paragrafo por um unico run, mantendo a formatacao do primeiro"""
    runs = [r for r in re.findall(r"<w:r[ >].*?</w:r>", p, re.S) if "<w:t" in r]
    if not runs:
        return p
    rpr = re.search(r"<w:rPr>.*?</w:rPr>", runs[0], re.S)
    p = p.replace(runs[0],
                  "<w:r>" + (rpr.group(0) if rpr else "") +
                  '<w:t xml:space="preserve">' + novo + "</w:t></w:r>", 1)
    for r in runs[1:]:
        p = p.replace(r, "", 1)
    return p


def fim_da_quebra_de_pagina(d):
    """indice logo apos o </w:p> do paragrafo que contem a 1a quebra de pagina.
    O pandoc escreve '<w:br w:type="page" />' com espaco; o Word, sem."""
    m = re.search(r'<w:br w:type="page"\s*/>', d)
    if not m:
        raise SystemExit("quebra de pagina da capa nao encontrada")
    return d.find("</w:p>", m.end()) + len("</w:p>")


def raiz_do_template():
    """atributos do elemento <w:document> do template (namespaces + mc:Ignorable)"""
    with zipfile.ZipFile(TEMPLATE) as z:
        x = z.read("word/document.xml").decode("utf-8")
    return re.search(r"<w:document[^>]*>", x).group(0)


def ajusta_namespaces(d):
    """o pandoc declara 9 namespaces; a capa do template usa mc:/wps:/wp14:.
    Sem as declaracoes o XML fica invalido e o Word recusa o arquivo."""
    atual = re.search(r"<w:document[^>]*>", d).group(0)
    ns = dict(re.findall(r'xmlns:([\w]+)="([^"]+)"', atual))
    ns.update(dict(re.findall(r'xmlns:([\w]+)="([^"]+)"', raiz_do_template())))
    ign = re.search(r'mc:Ignorable="([^"]+)"', raiz_do_template())
    novo = ("<w:document " +
            " ".join(f'xmlns:{k}="{v}"' for k, v in sorted(ns.items())) +
            (f' mc:Ignorable="{ign.group(1)}"' if ign else "") + ">")
    return d.replace(atual, novo, 1), len(ns)


def capa_do_template():
    """devolve o XML da capa do template, do inicio do body ate a 1a quebra de pagina"""
    with zipfile.ZipFile(TEMPLATE) as z:
        d = z.read("word/document.xml").decode("utf-8")
    ini = d.find("<w:body>") + len("<w:body>")
    capa = d[ini:fim_da_quebra_de_pagina(d)]
    for velho, novo in (("[NOME DO PROJETO]", TITULO),
                        ("[NOME DO ALUNO]", ALUNO),
                        ("2025", ANO)):
        if velho not in capa:
            raise SystemExit(f"placeholder da capa nao encontrado no template: {velho}")
        capa = capa.replace(velho, novo)
    return capa


def fora_do_sumario(d, *marcadores):
    """tira paragrafos do campo TOC sem mudar a aparencia deles.
    O campo TOC coleta pelo nivel de topico (1 a 3); outlineLvl 9 = corpo de texto.
    A ordem dos filhos de w:pPr e validada pelo schema: outlineLvl vem antes de w:rPr."""
    n = 0
    for m in re.finditer(r"<w:p[ >].*?</w:p>", d, re.S):
        p = m.group(0)
        if "<w:outlineLvl" in p:
            continue
        alvo = any(x in texto_do_paragrafo(p) for x in marcadores) or                any(x in p for x in marcadores)
        if not alvo:
            continue
        lvl = '<w:outlineLvl w:val="9"/>'
        if "<w:pPr>" in p:
            if "<w:rPr>" in p:
                novo = p.replace("<w:rPr>", lvl + "<w:rPr>", 1)
            else:
                novo = p.replace("</w:pPr>", lvl + "</w:pPr>", 1)
        else:
            novo = p.replace("<w:p>", "<w:p><w:pPr>" + lvl + "</w:pPr>", 1)
        d = d.replace(p, novo, 1)
        n += 1
    return d, n


def ajusta_documento(caminho):
    d = open(caminho, encoding="utf-8").read()
    d, n_ns = ajusta_namespaces(d)

    # estilo de tabela do proprio template
    n_tab = len(re.findall(r'<w:tblStyle w:val="Table"\s*/>', d))
    d = re.sub(r'<w:tblStyle w:val="Table"\s*/>',
               '<w:tblStyle w:val="Tabelacomgrade" />', d)

    # o pandoc poe o sumario antes de tudo; ele vai para depois do historico
    m = re.search(r"<w:sdt>.*?</w:sdt>", d, re.S)
    if not m:
        raise SystemExit("campo TOC nao encontrado na saida do pandoc")
    toc = m.group(0).replace(
        '<w:t xml:space="preserve">Table of Contents</w:t>',
        '<w:t xml:space="preserve">Sumário</w:t>')
    d = d[:m.start()] + d[m.end():]

    # capa gerada pelo markdown -> capa do template.
    # o fim da capa e o inicio do paragrafo "Historico de alteracoes do documento"
    ini = d.find("<w:body>") + len("<w:body>")
    fim = None
    for m in re.finditer(r"<w:p[ >].*?</w:p>", d, re.S):
        if "Hist" in texto_do_paragrafo(m.group(0)) and "altera" in texto_do_paragrafo(m.group(0)):
            fim = m.start()
            break
    if fim is None:
        raise SystemExit("titulo 'Historico de alteracoes' nao encontrado; capa nao substituida")
    d = d[:ini] + capa_do_template() + d[fim:]

    # sumario logo apos a tabela de historico de alteracoes
    i = d.find("</w:tbl>") + len("</w:tbl>")
    d = d[:i] + PB + toc + PB + d[i:]

    # o proprio titulo do sumario e o historico nao devem constar no indice
    d, n_fora = fora_do_sumario(d, "Histórico de alterações", 'w:val="CabealhodoSumrio"')

    try:
        ET.fromstring(d)
    except ET.ParseError as e:
        raise SystemExit(f"XML invalido apos as correcoes: {e}")

    open(caminho, "w", encoding="utf-8").write(d)
    return n_tab, n_ns, n_fora


def ajusta_cabecalho(pasta):
    alvos = [("Projeto XXXX", PROJETO), ("Versão: 3.0", VERSAO), ("03/06/2025", DATA)]
    for nome in sorted(os.listdir(pasta)):
        if not nome.startswith("header") or not nome.endswith(".xml"):
            continue
        caminho = os.path.join(pasta, nome)
        d = open(caminho, encoding="utf-8").read()
        orig = d
        for p in re.findall(r"<w:p[ >].*?</w:p>", d, re.S):
            t = texto_do_paragrafo(p)
            for gatilho, novo in alvos:
                if gatilho in t:
                    d = d.replace(p, reescreve_paragrafo(p, novo), 1)
                    break
        if d != orig:
            open(caminho, "w", encoding="utf-8").write(d)


def reempacota(pasta, destino):
    if os.path.exists(destino):
        os.remove(destino)
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as zf:
        primeiro = "[Content_Types].xml"
        zf.write(os.path.join(pasta, primeiro), primeiro)
        for raiz, _, arquivos in os.walk(pasta):
            for a in arquivos:
                rel = os.path.relpath(os.path.join(raiz, a), pasta).replace(os.sep, "/")
                if rel != primeiro:
                    zf.write(os.path.join(raiz, a), rel)


def main():
    if not shutil.which("pandoc"):
        raise SystemExit("pandoc nao encontrado no PATH")
    tmp = tempfile.mkdtemp(prefix="dvp_")
    try:
        build_md = os.path.join(tmp, "build.md")
        prepara_markdown(build_md)

        bruto = os.path.join(tmp, "bruto.docx")
        subprocess.run(["pandoc", build_md,
                        "--from=markdown+pipe_tables+raw_attribute",
                        f"--reference-doc={TEMPLATE}",
                        "--toc", "--toc-depth=3",
                        f"--resource-path={os.path.join(RAIZ, 'docs')}",
                        "-o", bruto], check=True)

        desempacotado = os.path.join(tmp, "unpacked")
        with zipfile.ZipFile(bruto) as z:
            z.extractall(desempacotado)

        n_tab, n_ns, n_fora = ajusta_documento(os.path.join(desempacotado, "word", "document.xml"))
        ajusta_cabecalho(os.path.join(desempacotado, "word"))
        reempacota(desempacotado, SAIDA)

        print(f"gerado: {SAIDA}")
        print(f"  {os.path.getsize(SAIDA):,} bytes | {n_tab} tabelas re-estilizadas | {n_ns} namespaces | {n_fora} fora do indice")
        print("  abra no Word e tecle Ctrl+A depois F9 para preencher o sumario")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
