# RoboCup Small Size League rules

English | [Japanese](README_jp.md)

This is the AsciiDoc source for the unofficial Japanese translation of RoboCup Small Size League rules.  
The official rules can be found at [Official GitHub Repository](https://github.com/RoboCup-SSL/ssl-rules)
The legacy version of the rules can be found at [here](https://github.com/RoboCup-SSL/ssl-rules-legacy)

## Build

The rules are automatically built on updates to the master-jp branch and published to [Github Pages](https://kkimurak.github.io/ssl-rules-ja/sslrules.html). There is also a [PDF-version](https://kkimurak.github.io/ssl-rules-ja/sslrules.pdf).  
You must use "allow-uri-read" option because we use the feature, of AsciiDoc, ["Include content from URI"](https://asciidoctor.org/docs/user-manual/#include-uri) to apply translations to built-in attributes (such as "Figure", "Table of Contents", etc.).

### Using AsciiDoctor natively

Install [AsciiDoctor](https://asciidoctor.org/) on your system . Afterwards, build HTML5 version with

```sh
# Build the HTML5 version
asciidoctor -a allow-uri-read sslrules.adoc
```

To build PDF version with Japanese characters, you can use asciidoctor-pdf-cjk-kai_gen_gothic.

```sh
# Build the PDF version
asciidoctor-pdf -r asciidoctor-pdf-cjk-kai_gen_gothic -a pdf-style=KaiGenGothicJP -a allow-uri-read sslrules.adoc
```

### Using docker image

If you have Docker installed, you can use the AsciiDoctor image that optimized for Japanese:

```sh
# Pull image once
docker pull htakeuchi/docker-asciidoctor-jp
# Build the HTML5 version
docker run -v $PWD:/documents/ htakeuchi/docker-asciidoctor-jp asciidoctor -r asciidoctor-diagram -a allow-uri-read sslrules.adoc
# Build the PDF version
docker run -v $PWD:/documents/ htakeuchi/docker-asciidoctor-jp asciidoctor-pdf -r asciidoctor-diagram -r asciidoctor-pdf-cjk-kai_gen_gothic -a pdf-style=KaiGenGothicJP -a allow-uri-read sslrules.adoc
```
