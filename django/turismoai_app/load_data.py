from turismoai_app.models import (
    Restaurante, 
    AtraccionTuristica, 
    ActividadAireLibre,
    CulturaOcio,
    Compras,
    VidaNocturna
)

def load_data():
    # Primero, limpiamos los datos existentes
    Restaurante.objects.all().delete()
    AtraccionTuristica.objects.all().delete()
    ActividadAireLibre.objects.all().delete()
    CulturaOcio.objects.all().delete()
    Compras.objects.all().delete()
    VidaNocturna.objects.all().delete()

    # Datos de Restaurantes
    restaurantes = [
        {
            "nombre": "La Abadía",
            "tipo_cocina": "Local e internacional",
            "direccion": "Avenida 3 Independencia, Mérida, Venezuela",
            "horario": "Abierto para almuerzo y cena",
            "opiniones": "Conocido por su ambientación sacra y decoración de monasterios. Excelente servicio y deliciosa comida."
        },
        {
            "nombre": "Dog And Ball",
            "tipo_cocina": "Comida rápida",
            "direccion": "Mérida, Venezuela",
            "horario": "Abierto para almuerzo, cena y hasta tarde",
            "opiniones": "Buen lugar para comida rápida con opciones de comida para llevar y acepta tarjetas de crédito."
        },
        {
            "nombre": "Heladería Coromoto",
            "tipo_cocina": "Postres",
            "direccion": "Mérida, Venezuela",
            "horario": "Abierto para desayuno, almuerzo y cena",
            "opiniones": "Famosa por tener el récord Guinness por la mayor variedad de sabores de helado."
        },
        {
            "nombre": "Avila Burger Mérida",
            "tipo_cocina": "Sudamericana",
            "direccion": "Mérida, Venezuela",
            "horario": "Abierto para almuerzo y cena",
            "opiniones": "Conocido por sus hamburguesas y comida sudamericana."
        },
        {
            "nombre": "La Parroquia",
            "tipo_cocina": "Temática",
            "direccion": "Mérida, Venezuela",
            "horario": "Abierto para eventos y cumpleaños",
            "opiniones": "Restaurante temático con ambiente de superhéroes, ideal para eventos y cumpleaños."
        }
    ]

    # Crear restaurantes
    for data in restaurantes:
        Restaurante.objects.create(**data)
    print("Restaurantes creados exitosamente")

    # Datos de Atracciones Turísticas
    atracciones = [
        {
            "nombre": "Teleférico de Mérida",
            "descripcion": "El Teleférico de Mérida es una de las principales atracciones turísticas de la ciudad. Ofrece vistas impresionantes de la cordillera andina y es el teleférico más alto y largo del mundo.",
            "horario": "Horario variable según la estación del año",
            "precio": 20.00,
            "opiniones": "Una experiencia impresionante con vistas panorámicas espectaculares."
        },
        {
            "nombre": "Parque Nacional Sierra Nevada",
            "descripcion": "Este parque nacional es ideal para los amantes de la naturaleza. Ofrece senderos para caminatas, avistamiento de aves y una rica biodiversidad.",
            "horario": "Abierto todo el día",
            "precio": 10.00,
            "opiniones": "Un lugar perfecto para conectarse con la naturaleza y disfrutar de la belleza de los Andes."
        },
        {
            "nombre": "Jardín Botánico de Mérida",
            "descripcion": "El Jardín Botánico de Mérida es un espacio dedicado a la conservación y estudio de la flora andina. Cuenta con más de 1200 especies de plantas.",
            "horario": "Abierto de 8:00 AM a 5:00 PM",
            "precio": 5.00,
            "opiniones": "Un lugar tranquilo y educativo para aprender sobre la flora de la región."
        }
    ]

    # Crear atracciones
    for data in atracciones:
        AtraccionTuristica.objects.create(**data)
    print("Atracciones turísticas creadas exitosamente")

    # Datos de Actividades al Aire Libre
    actividades = [
        {
            "nombre": "Rafting en los ríos de montaña",
            "descripcion": "Disfruta de una emocionante aventura de rafting en los ríos de montaña de Mérida. Ideal para amantes de la adrenalina.",
            "horario": "Horarios variables según la temporada",
            "equipo_necesario": "Chaleco salvavidas, casco, remo",
            "nivel_dificultad": "intermedio",
            "opiniones": "Una experiencia llena de adrenalina y diversión."
        },
        {
            "nombre": "Parapente desde las alturas",
            "descripcion": "Vuela sobre los paisajes andinos en una experiencia de parapente. Disfruta de vistas panorámicas y la emoción del vuelo libre.",
            "horario": "Horarios variables según la temporada",
            "equipo_necesario": "Parapente, casco, arnés",
            "nivel_dificultad": "avanzado",
            "opiniones": "Una actividad emocionante para los amantes de la aventura."
        },
        {
            "nombre": "Senderismo en el Páramo de la Culata",
            "descripcion": "Explora los paisajes únicos del Páramo de la Culata en una caminata guiada. Ideal para amantes de la naturaleza y el senderismo.",
            "horario": "Horarios variables según la temporada",
            "equipo_necesario": "Ropa abrigada, calzado adecuado, mochila",
            "nivel_dificultad": "principiante",
            "opiniones": "Una caminata tranquila con vistas impresionantes."
        }
    ]

    # Crear actividades
    for data in actividades:
        ActividadAireLibre.objects.create(**data)
    print("Actividades al aire libre creadas exitosamente")

    # Datos de Cultura y Ocio
    cultura = [
        {
            "nombre": "Museo Arqueológico de Mérida",
            "tipo": "museo",
            "descripcion": "Un museo dedicado a la historia arqueológica de la región andina de Venezuela.",
            "horario": "Abierto de 9:00 AM a 5:00 PM",
            "precio": 3.00,
            "opiniones": "Un lugar fascinante para aprender sobre la historia arqueológica de Mérida."
        },
        {
            "nombre": "Teatro César Rengifo",
            "tipo": "teatro",
            "descripcion": "Un teatro histórico que ofrece una variedad de espectáculos culturales y artísticos.",
            "horario": "Horarios variables según la programación",
            "precio": 10.00,
            "opiniones": "Un lugar icónico para disfrutar de espectáculos culturales y artísticos."
        }
    ]

    # Crear cultura
    for data in cultura:
        CulturaOcio.objects.create(**data)
    print("Lugares culturales creados exitosamente")

    # Datos de Compras
    tiendas = [
        {
            "nombre": "Supermercado Online con Delivery Gratis",
            "direccion": "Mérida, Venezuela",
            "horario": "Abierto todo el día",
            "productos": "Productos frescos, viveres, carnes y todo lo que necesitas para tu casa.",
            "opiniones": "Excelente servicio de entrega gratuita en todo el país."
        },
        {
            "nombre": "Tu Gente Venezuela",
            "direccion": "Mérida, Venezuela",
            "horario": "Abierto todo el día",
            "productos": "Productos y servicios de calidad a domicilio en 24 horas.",
            "opiniones": "Servicio rápido y eficiente con productos de alta calidad."
        }
    ]

    # Crear tiendas
    for data in tiendas:
        Compras.objects.create(**data)
    print("Tiendas creadas exitosamente")

    # Datos de Vida Nocturna
    bares = [
        {
            "nombre": "Whisky Bar",
            "tipo": "bar",
            "direccion": "Centro Comercial Mayeya HRVV+J65 Av. Las Américas Mérida 5101",
            "horario": "Jueves, viernes y sábados a partir de las 10:00 PM",
            "precio_entrada": 10.00,
            "opiniones": "El epicentro de la vida nocturna en Mérida con un ambiente vibrante y contagioso."
        },
        {
            "nombre": "La Hatch",
            "tipo": "pub",
            "direccion": "Hotel Fiesta Americana, Mérida",
            "horario": "Abierto todo el día",
            "precio_entrada": 5.00,
            "opiniones": "Un bar acogedor con atención personalizada y excelente oferta de bebidas."
        }
    ]

    # Crear bares
    for data in bares:
        VidaNocturna.objects.create(**data)
    print("Lugares de vida nocturna creados exitosamente")

if __name__ == "__main__":
    load_data() 