from utils_operation_net import *
def print_in_output_file_name_from_line1_current_column(file_out, map_data_for_write_in_output):
    parts_command_str = ['ADD SECTION:POOLNAME=\"',
                         '\",SECTIONNUM=',
                         ',IPVERSION=IPV4,V4STARTIP=\"',
                         '\",V4ENDIP=\"',
                         '\";\n']

    for key in sorted(map_data_for_write_in_output.keys()):
        line_out_str = []
        array_network = map_data_for_write_in_output[key]

        j = 0
        for i in range(0, len(array_network)):

            for k in range(0, 2):
                line_out_str.append(parts_command_str[0])
                line_out_str.append(key)
                line_out_str.append(parts_command_str[1])
                line_out_str.append(j)
                j = j + 1
                list_addition_parameter_network_first_ip, list_addition_parameter_network_last_ip = network_first_last(
                    array_network[i])
                line_out_str.append(parts_command_str[2])
                line_out_str.append(list_addition_parameter_network_first_ip[k])
                line_out_str.append(parts_command_str[3])
                line_out_str.append(list_addition_parameter_network_last_ip[k])
                line_out_str.append(parts_command_str[4])
        aggregated_array_network = aggregate_networks(array_network)
        with open(file_out, 'a') as file:
            line_out_str = [str(x) for x in line_out_str]
            file.write(''.join(line_out_str))
            line_out_str = [str(x) for x in line_data_of_network_aggregation(aggregated_array_network)]
            file.write(''.join(line_out_str))

    return


def line_data_of_network_aggregation(network_agregation_array):
    line_out_str=[]
    parts_command_str = ['ADD AGGREGATEROUTE:VRFNAME=\"gi_vpcef_\",AFTYPE=ipv4uni,AGGREADDRESS=\"',
                         '\",MASKLENGTH=',
                         ',ASSETENABLE=FALSE,DETAILSUPPRESSED=TRUE;\n']
    for network in network_agregation_array:
        line_out_str.append(parts_command_str[0])
        print('network:', network)
        line_out_str.append(network.network_address)
        line_out_str.append(parts_command_str[1])
        line_out_str.append(network.prefixlen)
        line_out_str.append(parts_command_str[2])

    return line_out_str
