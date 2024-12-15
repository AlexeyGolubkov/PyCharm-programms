import ipaddress
def aggregate_and_return_remaining_networks(networks):
    # Создаем копию исходного списка сетей, чтобы избежать изменения оригинального списка
    remaining_networks = networks.copy()
    print('remaining_networks:', remaining_networks)
    network_objects = []
    for network_str in remaining_networks:
        try:
            network_object = ipaddress.ip_network(network_str)
            network_objects.append(network_object)
        except ValueError as e:
            print(f"Ошибка при обработке сети {network_str}: {e}")
    # Агрегируем сети
    aggregated_networks = list(ipaddress.collapse_addresses(network_objects))

    # # Удаляем агрегированные сети из списка оставшихся
    # for network in aggregated_networks:
    #     non_subnets = []
    #     for subnet in remaining_networks:
    #         if not subnet.subnet_of(network):
    #             non_subnets.append(subnet)
    #     remaining_networks = non_subnets

    return aggregated_networks, remaining_networks

def network_first_last(networks):
    # network = ipaddress.IPv4Network(networks)
    network = ipaddress.ip_network(networks)
    first_ip_str = []
    last_ip_str = []
    # Разделение сети на две равные части
    new_prefix = network.prefixlen + 1
    subnets = list(network.subnets(new_prefix=new_prefix))

    for network in subnets:
        # Первый IP-адрес в сети (начало диапазона)
        first_ip_str.append(str(network.network_address))
        # Последний IP-адрес в сети (конец диапазона)
        last_ip_str.append(str(network.broadcast_address))

    return first_ip_str, last_ip_str