import ipaddress
from collections import defaultdict
import copy


def print_in_output_file_name_from_line1_current_column(file_out, map_data_for_write_in_output):
    parts_command_str = ['ADD SECTION:POOLNAME=\"'
        , '\",SECTIONNUM='
        , ',IPVERSION=IPV4,V4STARTIP=\"'
        , '\",V4ENDIP=\"'
        , '\";\n']

    list_addition_parameter_network_begin_last = []

    for key in sorted(map_data_for_write_in_output.keys()):
        line_out_str = []
        array_network = map_data_for_write_in_output[key]
        j=0
        for i in range(0, len(array_network)):

            for k in range (0,2):
                line_out_str.append(parts_command_str[0])
                line_out_str.append(key)
                line_out_str.append(parts_command_str[1])
                line_out_str.append(j)
                j=j+1
                list_addition_parameter_network_first_ip,list_addition_parameter_network_last_ip = network_first_last(array_network[i])
                line_out_str.append(parts_command_str[2])
                line_out_str.append(list_addition_parameter_network_first_ip[k])
                line_out_str.append(parts_command_str[3])
                line_out_str.append(list_addition_parameter_network_last_ip[k])
                line_out_str.append(parts_command_str[4])
        with open(file_out, 'a') as file:
            print(line_out_str)
            d=0
            line_out_str = [str(x) for x in line_out_str]
            file.write(''.join(line_out_str))

    return


def network_first_last(networks):
    network = ipaddress.IPv4Network(networks)
    first_ip_str = []
    last_ip_str = []
    # Разделение сети на две равные части
    new_prefix = network.prefixlen + 1
    subnets = list(network.subnets(new_prefix=new_prefix))

    for network in subnets:
        # Первый IP-адрес в сети (начало диапазона)
        first_ip_str.append(str (network.network_address))
        # Последний IP-адрес в сети (конец диапазона)
        last_ip_str.append(str (network.broadcast_address))

    return first_ip_str, last_ip_str

# def print_in_output_file_name_data_of_network_agregation(file_out, network_agregation_array):
#     str1 = 'ADD AGGREGATEROUTE:VRFNAME=\"gi_vpcef_\",AFTYPE=ipv4uni,AGGREADDRESS=\"'
#     str2 = '\",MASKLENGTH='
#     str3 = ',ASSETENABLE=FALSE,DETAILSUPPRESSED=TRUE;\n'
#
#     with open(file_out, 'a') as file:
#         # subprogram_agregation_network
#         file.write(str1 + str(network.network_address) + str2 + str(network.prefixlen) + str3)
#
#     return
