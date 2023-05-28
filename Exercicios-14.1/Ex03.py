def converte_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60

    tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    return tempo_formatado

print(converte_tempo(3661))  # Resultado: "01:01:01"
print(converte_tempo(7200))  # Resultado: "02:00:00"
print(converte_tempo(180))   # Resultado: "00:03:00"