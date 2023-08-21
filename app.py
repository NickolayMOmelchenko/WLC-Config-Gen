from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route('/')
def index():
    # Render the index.html page
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Retrieve form data from the request
    wlc_name = request.form['wlc_name']
    wlc_type = request.form['wlc_type']
    AAA_server_name = request.form['AAA_server_name']
    AAA_IPv4_address = request.form['AAA_IPv4_address']
    Shared_Secret = request.form['Shared_Secret']
    AAA_server_group_name = request.form['AAA_server_group_name']
    dot1x_list_name = request.form['dot1x_list_name']
    wlan_profile_name = request.form['wlan_profile_name']
    wlan_id = request.form['wlan_id']
    wlan_ssid = request.form['wlan_ssid']
    policy_profile_name = request.form['policy_profile_name']
    vlanID_or_VLAN_name = request.form['vlanID_or_VLAN_name']
    policy_tag_name = request.form['policy_tag_name']
    ethernet_mac_addr = request.form['ethernet_mac_addr']

    # Generate commands for each configuration step
    command1 = generate_command1(wlc_name)
    command2 = generate_command2(wlc_type)
    command3 = generate_command3(AAA_server_name)
    command4 = generate_command4(AAA_IPv4_address)
    command5 = generate_command5(Shared_Secret)
    command6 = generate_command6(AAA_server_group_name, AAA_server_name, AAA_IPv4_address, Shared_Secret)
    command7 = generate_command7(dot1x_list_name, AAA_server_group_name)
    command8 = generate_command8(wlan_profile_name)
    command9 = generate_command9(wlan_id)
    command10 = generate_command10(wlan_ssid)
    command11 = generate_command11(policy_profile_name, dot1x_list_name)
    command12 = generate_command12(vlanID_or_VLAN_name)
    command13 = generate_command13(policy_tag_name, wlan_profile_name, policy_profile_name)
    command14 = generate_command14(ethernet_mac_addr, policy_tag_name)

    # Render the commands template with the generated commands
    return render_template('commands.html',
                           wlc_name=wlc_name,
                           wlc_type=wlc_type,
                           AAA_server_name=AAA_server_name,
                           AAA_IPv4_address=AAA_IPv4_address,
                           Shared_Secret=Shared_Secret,
                           AAA_server_group_name=AAA_server_group_name,
                           dot1x_list_name=dot1x_list_name,
                           wlan_profile_name=wlan_profile_name,
                           wlan_id=wlan_id,
                           wlan_ssid=wlan_ssid,
                           policy_profile_name=policy_profile_name,
                           vlanID_or_VLAN_name=vlanID_or_VLAN_name,
                           policy_tag_name=policy_tag_name,
                           ethernet_mac_addr=ethernet_mac_addr,
                           command1=command1,
                           command2=command2,
                           command3=command3,
                           command4=command4,
                           command5=command5,
                           command6=command6,
                           command7=command7,
                           command8=command8,
                           command9=command9,
                           command10=command10,
                           command11=command11,
                           command12=command12,
                           command13=command13,
                           command14=command14
                           )

# Download Command
def generate_command1(wlc_name):
    # Generate command for setting the WLC name
    command1 = ("enable\n" + "configure terminal\n" + 'hostname ' + wlc_name + '\n' + "aaa new-model")
    return command1

def generate_command2(wlc_type):
    # Generate the appropriate command based on the WLC type
    command2 = ''
    if wlc_type == 'WLC-9800':
        command2 = ''  # Replace with the correct command for wlc-9800
    elif wlc_type == 'option2':
        command2 = ''  # Replace with the correct command for option2
    elif wlc_type == 'option3':
        command2 = ''  # Replace with the correct command for option3
    return command2

def generate_command3(AAA_server_name):
    # Generate the command for configuring the AAA server name
    command3 = 'radius server ' + AAA_server_name
    return command3

def generate_command4(AAA_IPv4_address):
    # Generate the command for configuring the AAA server IPv4 address and ports
    command4 = ('address ipv4 ' + AAA_IPv4_address + ' auth-port 1812 acct-port 1813\n'
                 + "timeout 300\n" + "retransmit 3" )
    return command4

def generate_command5(Shared_Secret):
    # Generate the command for configuring the shared secret key
    command5 = 'key ' + Shared_Secret + "\n" + "exit\n"
    return command5

def generate_command6(AAA_server_group_name, AAA_server_name, AAA_IPv4_address, Shared_Secret):
    # Generate commands for configuring AAA server group and dynamic authorization
    command6 = ('aaa group server radius ' + AAA_server_group_name + "\n" + "server name " + AAA_server_name + "\n" + "exit\n"
                + 'aaa server radius dynamic-author\n' + "client " + AAA_IPv4_address
                + " server-key " + Shared_Secret + "\n")
    return command6

def generate_command7(dot1x_list_name, AAA_server_group_name):
    # Generate command for configuring 802.1x authentication and associating with the AAA server group
    command7 = ("aaa authentication dot1x " + dot1x_list_name + " group " + AAA_server_group_name
                + "\nradius-server dead-criteria time 5 tries 3\n"
                + "radius-server deadtime 5\nexit\n" )
    return command7

def generate_command8(wlan_profile_name):
    # Generate command based on the WLAN profile name 
    command8 = 'config t' + "\nwlan " + wlan_profile_name
    return command8

def generate_command9(wlan_id):
    # Generate command based on the WLAN ID
    command9 = " " + wlan_id
    return command9

def generate_command10(wlan_ssid):
    # Generate command based on the SSID 
    command10 = " " + wlan_ssid
    return command10

def generate_command11(policy_profile_name, dot1x_list_name):
    # Generate command based on the name of the policy profile and name of dot1x list 
    command11 = ('security dot1x authentication-list ' + dot1x_list_name + "\nno shutdown\n" + "config t\n"
                + "wireless profile policy " + policy_profile_name + "\naaa-override\ncentral switching\n")
    return command11

def generate_command12(vlanID_or_VLAN_name):
    # Generate command based on the vlan ID/Name
    command12 = 'vlan ' + vlanID_or_VLAN_name + "\nno shutdown"
    return command12

def generate_command13(policy_tag_name, wlan_profile_name, policy_profile_name):
    # Generate command based on the policy profile name, tag, and profile name
    command13 = ('wireless tag policy ' + policy_tag_name
                 + ' \nwlan ' + wlan_profile_name + ' policy ' + policy_profile_name)
    return command13

def generate_command14(ethernet_mac_addr, policy_tag_name):
    # Generate command based on the mac address and policy tag name
    command14 = 'ap ' + ethernet_mac_addr + '\npolicy-tag ' + policy_tag_name + '\nend'
    return command14


@app.route('/download', methods=['POST'])
def download():
    # Retrieve form data from the request
    wlc_name = request.form['wlc_name']
    wlc_type = request.form['wlc_type']
    AAA_server_name = request.form['AAA_server_name']
    AAA_IPv4_address = request.form['AAA_IPv4_address']
    Shared_Secret = request.form['Shared_Secret']
    AAA_server_group_name = request.form['AAA_server_group_name']
    dot1x_list_name = request.form['dot1x_list_name']
    wlan_profile_name = request.form['wlan_profile_name']
    wlan_id = request.form['wlan_id']
    wlan_ssid = request.form['wlan_ssid']
    policy_profile_name = request.form['policy_profile_name']
    vlanID_or_VLAN_name = request.form['vlanID_or_VLAN_name']
    policy_tag_name = request.form['policy_tag_name']
    ethernet_mac_addr = request.form['ethernet_mac_addr']

    # Generate commands for the download
    command1 = generate_command1(wlc_name)
    command2 = generate_command2(wlc_type)
    command3 = generate_command3(AAA_server_name)
    command4 = generate_command4(AAA_IPv4_address)
    command5 = generate_command5(Shared_Secret)
    command6 = generate_command6(AAA_server_group_name, AAA_server_name, AAA_IPv4_address, Shared_Secret)
    command7 = generate_command7(dot1x_list_name, AAA_server_group_name)
    command8 = generate_command8(wlan_profile_name)
    command9 = generate_command9(wlan_id)
    command10 = generate_command10(wlan_ssid)
    command11 = generate_command11(policy_profile_name, dot1x_list_name)
    command12 = generate_command12(vlanID_or_VLAN_name)
    command13 = generate_command13(policy_tag_name, wlan_profile_name, policy_profile_name)
    command14 = generate_command14(ethernet_mac_addr, policy_tag_name)
    # Combine all commands into a single string
    command_string = command1 + '\n' + command2 + '\n' + command3 + '\n' + command4 + '\n' + command5 + '\n' + command6 + '\n' + command7 + '\n' + command8  + command9  + command10 + '\n' + command11 + '\n' + command12 + '\n' + command13 + '\n' + command14

    # Create a response with the command string and set appropriate headers for downloading as a text file
    response = Response(command_string, mimetype='text/plain')
    response.headers.set("Content-Disposition", "attachment", filename="commands.txt")

    return response

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
