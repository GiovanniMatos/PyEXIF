import exifread

# Abrir a imagem em modo binário
with open(r"exemplo.png", 'rb') as image_file:
    # Ler os metadados EXIF da imagem
    tags = exifread.process_file(image_file)

    # Verificar se há metadados EXIF
    if tags:
        # Iterar sobre as tags de metadados EXIF
        for tag, value in tags.items():
            print(f'{tag}: {value}')
    else:
        print('A imagem não contém metadados EXIF.')

    if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
            latitude = tags['GPS GPSLatitude']
            longitude = tags['GPS GPSLongitude']

            # Converter as coordenadas de formato de lista para decimal
            latitude = float(latitude.values[0].num) / float(latitude.values[0].den)
            longitude = float(longitude.values[0].num) / float(longitude.values[0].den)

            print(f'Latitude: {latitude}')
            print(f'Longitude: {longitude}')
    else:
        print('As coordenadas geográficas não estão disponíveis na imagem.')