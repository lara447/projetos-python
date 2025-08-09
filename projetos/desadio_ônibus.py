preco_da_passagem = 5.00
preco_do_diesel = 5.95

onibus = [
    {"onibus1": {"capacidade": 65, "consumo": 11, "manutencao": 80}},
    {"onibus2": {"capacidade": 50, "consumo": 8, "manutencao": 60}},
    {"onibus3": {"capacidade": 40, "consumo": 6, "manutencao": 50}},
]

itinerario = [
    {"itinerario1": {"ida": 20, "volta": 20, "passageiros": 790}},
    {"itinerario2": {"ida": 25, "volta": 18, "passageiros": 1200}},
    {"itinerario3": {"ida": 32, "volta": 36, "passageiros": 835}},
]

for item_onibus in onibus:
    for nome_onibus, dados_onibus in item_onibus.items():
        capacidade = dados_onibus["capacidade"]
        consumo = dados_onibus["consumo"]
        manutencao = dados_onibus["manutencao"]
        print(f"\nÔnibus: {nome_onibus} | Capacidade: {capacidade}, Consumo: {consumo}, Manutenção: {manutencao}")
        
        for item_itinerario in itinerario:
            for nome_itinerario, dados_itinerario in item_itinerario.items():
                ida = dados_itinerario["ida"]
                volta = dados_itinerario["volta"]
                passageiros = dados_itinerario["passageiros"]

                distancia_da_viagem = ida + volta
                viagens = (passageiros + capacidade - 1) // capacidade
                distancia_total = distancia_da_viagem * viagens

                litros_de_diesel = distancia_total / consumo
                custo_combustivel = litros_de_diesel * preco_do_diesel
                custo_total = custo_combustivel + manutencao
                receita = passageiros * preco_da_passagem
                lucro = receita - custo_total

                print(f"\nItinerário: {nome_itinerario}")
                print(f"Viagens por dia: {viagens}")
                print(f"Distância total: {distancia_total}km")
                print(f"Litros de diesel consumidos: {litros_de_diesel:.2f}L")
                print(f"Custo total: R${custo_total:.2f}")
                print(f"Receita total: R${receita:.2f}")
                print(f"Lucro total: R${lucro:.2f}")
