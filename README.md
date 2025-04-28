# Readnator

## Descrição

Readnator é um script Python simples que percorre um diretório, permitindo que você selecione interativamente quais arquivos de código e subdiretórios incluir em um relatório de texto. Ele é útil para consolidar o conteúdo de vários arquivos de código em um único documento, facilitando a revisão ou o compartilhamento. O script oferece opções para processamento automático de arquivos de código e para incluir ou excluir arquivos e diretórios ocultos. Notebooks Jupyter (`.ipynb`) são tratados especialmente, removendo outputs e números de execução para focar apenas no código.

### Para que serve
Serve para após o txt feito, usar ele junto a uma IA generativa e criar um `README.md` para seu projeto. 

## Funcionalidades

*   **Processamento interativo ou automático:** Escolha processar arquivos individualmente ou automaticamente com base nas extensões configuradas.
*   **Suporte a diversas linguagens de programação e formatos de arquivo:** Compatível com extensões comuns de código e texto como `.py`, `.js`, `.html`, `.css`, `.json`, `.md`, e mais.
*   **Relatórios organizados:** Gera um relatório de texto formatado com cabeçalhos para diretórios e arquivos, facilitando a leitura e navegação.
*   **Tratamento especial para Notebooks Jupyter (`.ipynb`):** Remove outputs de células de código e contagens de execução para um relatório mais limpo focado no código fonte.
*   **Opção para incluir arquivos e diretórios ocultos:** Flexibilidade para processar ou ignorar arquivos e diretórios que começam com ponto (`.`).
*   **Lista de bloqueio e lista de extensões permitidas/ignoradas:** Personalize o comportamento do script definindo arquivos/diretórios a serem sempre ignorados e as extensões a serem processadas automaticamente.
*   **Detecção de encoding:** Tenta ler arquivos com `utf-8` e, em caso de falha, tenta com `latin-1` para lidar com diferentes codificações de texto.
*   **Relatórios salvos em pasta dedicada:** Os relatórios são gerados e salvos em uma pasta `relatorios` dentro do diretório de execução do script, mantendo os arquivos organizados.

## Como usar

1.  **Clone ou baixe o repositório:** Obtenha os arquivos do Readnator.
2.  **Navegue até o diretório `Readnator`:** Abra o terminal ou prompt de comando e vá para a pasta onde você salvou os arquivos.
3.  **Execute o script `app.py`:**

    ```bash
    python Readnator/app.py
    ```

4.  **Siga as instruções no terminal:**

    *   O script perguntará se você deseja processar todos os arquivos de código automaticamente. Responda `Y` ou `n`.
        *   Se escolher `Y`, todos os arquivos com extensões na lista `ALLOWED_EXTENSIONS` serão processados automaticamente.
        *   Se escolher `n`, você será perguntado para cada arquivo de código se deseja processá-lo.
    *   Em seguida, perguntará se deseja incluir arquivos/diretórios ocultos. Responda `y` ou `N`.
        *   Se escolher `y`, arquivos e diretórios que começam com `.` serão incluídos no processamento.
        *   Se escolher `N`, eles serão ignorados (a menos que explicitamente processados interativamente).
    *   Para cada diretório, o script perguntará se você deseja entrar nele. Responda `Y` ou `n`.
    *   Para cada arquivo de código (se o processamento automático não estiver ativado), o script perguntará se você deseja processá-lo. Responda:
        *   `Y` ou pressione Enter para processar o arquivo.
        *   `n` para ignorar o arquivo.
        *   `a` para ativar o processamento automático para os arquivos restantes.

5.  **Verifique a pasta `relatorios`:** Após a execução, o relatório de texto será gerado e salvo na pasta `relatorios` dentro do diretório onde você executou o script. O nome do arquivo de relatório será o mesmo nome do diretório raiz que você processou (ex: `NomeDoDiretorio.txt`).

## Configuração

Você pode personalizar o comportamento do Readnator modificando as seguintes variáveis no arquivo `Readnator/app.py`:

*   **`local`:** Local onde o repositorio está.
*   **`BLACKLIST`:** Conjunto de nomes de arquivos e diretórios que serão sempre ignorados. Útil para excluir pastas como `.git`, `venv`, `node_modules`, etc.
*   **`ALLOWED_EXTENSIONS`:** Conjunto de extensões de arquivo que serão automaticamente processadas quando a opção de processamento automático for ativada.
*   **`IGNORED_EXTENSIONS`:** Conjunto de extensões de arquivo que serão sempre ignoradas, independentemente das opções interativas ou automáticas.
*   **`OUTPUT_FOLDER`:** Nome da pasta onde os relatórios de texto serão salvos. O padrão é `relatorios`.

Edite diretamente o arquivo `Readnator/app.py` para ajustar essas configurações às suas necessidades.

## Exemplo

Suponha que você queira gerar um relatório dos arquivos de código no diretório `MeuProjeto`.

1.  Execute o script `Readnator/app.py` dentro do diretório que contém `MeuProjeto`.
2.  Quando solicitado "Deseja processar todos os arquivos de código automaticamente? [Y/n]", responda `n` para processar interativamente.
3.  Quando solicitado "Deseja incluir arquivos/diretórios ocultos? [y/N]", responda `N` para ignorar arquivos ocultos.
4.  O script começará a percorrer o diretório `MeuProjeto` e perguntará se você deseja entrar em cada subdiretório e processar cada arquivo de código. Responda de acordo com suas necessidades.
5.  Após a conclusão, um arquivo chamado `MeuProjeto.txt` será gerado na pasta `relatorios` contendo o conteúdo dos arquivos que você selecionou.
