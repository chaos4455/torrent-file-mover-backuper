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
