# 🗂️ Torrent File Mover

## 📜 Descrição

**Torrent File Mover** é uma ferramenta prática desenvolvida em Python que permite **fazer backup dos arquivos `.torrent`** da pasta AppData do uTorrent. Este projeto visa ajudar os usuários a manter seus arquivos de torrent organizados e seguros, evitando a perda de referências durante o download.

⚠️ **Atenção:** **Não execute esta ferramenta enquanto houver torrents em download**, pois isso pode fazer com que o torrent perca a referência. Se isso acontecer, você precisará apagar o torrent em download com erro e executar o arquivo diretamente pela pasta onde está o `.torrent`.

---

## 🚀 Funcionalidades

- **Backup Automático**: Move todos os arquivos `.torrent` da pasta AppData para uma localização segura e organizada.
- **Facilidade de Uso**: Interface simples, disponível como um executável para facilitar o uso por qualquer usuário.
- **Organização de Arquivos**: Os arquivos são movidos para `C:\torrentsexportados`, mantendo seu sistema limpo e livre de arquivos desnecessários.

---

## 📦 Requisitos

Para utilizar esta ferramenta, você precisará ter:

- **Python 3.x**: O script é desenvolvido em Python, por isso é necessário ter uma versão compatível instalada em seu sistema.

### 🔧 Bibliotecas Necessárias

Além do Python, não são necessárias bibliotecas externas, pois utilizamos apenas as bibliotecas padrão:

- `os`
- `shutil`

---

## 📥 Download do Executável

Você pode baixar a última versão do executável diretamente do repositório. Clique no link abaixo para fazer o download:

[**Download Último Executável**](https://github.com/chaos4455/torrent-file-mover-backuper/releases/latest)

---

## ⚙️ Como Usar

### Passo a Passo

1. **Certifique-se** de que não há torrents em download no uTorrent.
2. **Baixe o executável** do link acima.
3. **Execute o programa** clicando duas vezes no arquivo `.exe`.
4. Os arquivos `.torrent` serão movidos para `C:\torrentsexportados`.

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
