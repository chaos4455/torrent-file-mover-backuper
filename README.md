# 🗂️ Torrent File Mover

## 📜 Descrição

**Torrent File Mover** é uma ferramenta prática desenvolvida em Python que permite **fazer backup dos arquivos `.torrent`** da pasta AppData do uTorrent. Este projeto visa ajudar os usuários a manter seus arquivos de torrent organizados e seguros, para uso posterior, re-download, se necessário.

⚠️ **Atenção:** **Não execute esta ferramenta enquanto houver torrents em download**, pois isso pode fazer com que o torrent perca a referência. Se isso acontecer, você precisará apagar o torrent em download com erro e executar o arquivo diretamente pela pasta onde está o `.torrent`, no caso C:\torrentsexportados.

---

## 🚀 Funcionalidades

- **Backup Automático**: Move todos os arquivos `.torrent` da pasta AppData para uma localização segura e organizada.
- **Facilidade de Uso**: Interface simples, disponível como um executável para facilitar o uso por qualquer usuário.
- **Organização de Arquivos**: Os arquivos são movidos para `C:\torrentsexportados`, mantendo seu sistema limpo e livre de arquivos desnecessários.

---

## 📦 Requisitos

Para utilizar esta ferramenta, você precisará ter:

- **Python 3.x**: O script é desenvolvido em Python, por isso é necessário ter uma versão compatível instalada em seu sistema, somente se executar o .py, se for o exe não precisa do python instalado..

### 🔧 Bibliotecas Necessárias

Além do Python, não são necessárias bibliotecas externas, pois utilizamos apenas as bibliotecas padrão:

- `os`
- `shutil`

---

## 📥 Download do Executável

Você pode baixar a última versão do executável diretamente do repositório. Clique no link abaixo para fazer o download:

[**Download Último Executável**]([https://github.com/chaos4455/torrent-file-mover-backuper/releases/latest](https://github.com/chaos4455/torrent-file-mover-backuper/tree/main/programas))

---

## ⚙️ Como Usar

### Passo a Passo

1. **Certifique-se** de que não há torrents em download no uTorrent.
2. **Baixe o executável** do link acima.
3. **Execute o programa** clicando duas vezes no arquivo `.exe`.
4. Os arquivos `.torrent` serão movidos da pasta do utorrent em app data, para `C:\torrentsexportados`.

### Estrutura do Código

Aqui está um exemplo do código-fonte que executa a tarefa de mover os arquivos:

```python
import os
import shutil

# Caminhos das pastas
source_folder = os.path.join(os.environ['APPDATA'], 'uTorrent')
destination_folder = r'C:\torrentsexportados'

# Cria o diretório de destino se não existir
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move os arquivos .torrent
for filename in os.listdir(source_folder):
    if filename.endswith('.torrent'):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)
        shutil.move(src_path, dst_path)
        print(f'Movido: {filename} para {destination_folder}')

print('Todos os arquivos .torrent foram movidos com sucesso!')

```
## 🛠️ CI/CD com GitHub Actions

Neste repositório, utilizei o **GitHub Actions** para implementar práticas de **DevOps** e **CI/CD** (Integração Contínua/Entrega Contínua) para gerar o executável através do código fonte em python usando o ambiente windows, powershell e o pyinstaller, para compatibilidade com o ambiente windows. Abaixo está a configuração da ação que automatiza o processo de build do nosso executável, seguindo boas práticas de desenvolvimento e deploy de software usando o github como repositório e o github actions como builder e packager.

### 🔗 [Veja o Workflow Aqui](https://github.com/chaos4455/torrent-file-mover-backuper/blob/main/.github/workflows/build.yaml)

### ⚙️ Estrutura do Workflow

## 🗺️ Diagrama de Fluxo do Processo de Build

### 🔄 Etapas do Workflow

    A[🔍 Checkout Repository] --> B[🐍 Set Up Python]
    B --> C[⬆️ Upgrade pip]
    C --> D[📦 Install PyInstaller]
    D --> E[🛠️ Create Executable]
    E --> F[📁 Create Program Folder]
    F --> G[➡️ Move Executable]
    G --> H[➕ Add Programas Folder Changes]
    H --> I[👤 Configure Git User]
    I --> J[📝 Commit Changes]
    J --> K[🔼 Push Changes]
    K --> L[📤 Upload Executable]
    L --> M[✅ Build Complete!]

```yaml
name: Deploy Py to Exe

on:
  push:
    branches:
      - main  # O workflow é acionado em cada push para a branch principal.

jobs:
  build:
    runs-on: windows-latest  # A ação é executada em um ambiente Windows.

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2  # Faz o checkout do repositório.

    - name: Set Up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'  # Define a versão do Python a ser usada.

    - name: Upgrade pip
      run: |
        python -m pip install --upgrade pip  # Atualiza o pip para a versão mais recente.

    - name: Install PyInstaller
      run: |
        pip install pyinstaller  # Instala o PyInstaller para criar executáveis.

    - name: Create Executable
      run: |
        pyinstaller --onefile --windowed --icon=torrent-icon.ico py-torrent-file-mover.py  # Cria um executável único.

    - name: Create Program Folder if Not Exists
      run: |
        if (-Not (Test-Path -Path "programas")) { New-Item -ItemType Directory -Path "programas" }  # Cria a pasta 'programas' se não existir.

    - name: Move Executable to Programas Folder
      run: |
        move dist\\py-torrent-file-mover.exe programas\\  # Move o executável gerado para a pasta 'programas'.

    - name: Add Programas Folder Changes
      run: |
        git add programas  # Adiciona as mudanças na pasta 'programas' ao git.

    - name: Configure Git User
      run: |
        git config --local user.email 'github-actions[bot]@users.noreply.github.com'  # Configura o email do bot do GitHub.
        git config --local user.name 'github-actions[bot]'  # Configura o nome do bot do GitHub.

    - name: Commit Changes
      run: |
        git commit -m "Add new version of executável"  # Comita as mudanças realizadas na pasta 'programas'.

    - name: Push Changes
      run: |
        git push origin main  # Faz o push das mudanças para a branch principal.

    - name: Upload Executable
      uses: actions/upload-artifact@v2
      with:
        name: python-torrent-file-mover-backup-v01.exe  # Nome do artefato que será enviado.
        path: programas\\py-torrent-file-mover.exe  # Caminho do executável a ser enviado.

```


