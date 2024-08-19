import os
import sys
import time
import subprocess
import importlib.util

BOLD = '\033[1m'
RESET = '\033[0m'

selected_overclock = ""

def is_running_as_root(): #Checks to see if user is root
    return os.geteuid() == 0

def clear_screen(): #Function to clear screen when called
    os.system('cls' if os.name == 'nt' else 'clear')

def select_sbc(): #First screen. Will prompt user for SBC

    from colorama import Fore
    import pyfiglet

    styled_text=pyfiglet.figlet_format("SBCTuner", font = "slant") 
    print(Fore.RED + styled_text + Fore.RESET)
    print("#### Ver 0.01a  // Created by 0p3nARM ####\n\nWARMING: THIS PROGRAM WILL NOT AUTOMATICALLY DETECT YOU SBC AND EDIT CONFIG FILES. SELECTING THE INCORRECT SBC AND SETTINGS MAY OR WILL RESULT IN PERMENANT DAMAGE THAT VOIDS YOUR WARRENTY!\n\nSelect SBC:\n[1] Raspberry Pi\n[2] Orange Pi (Unavaliable)\n[3] Radxa (Unavaliable)\n[4] Milk V (Risc-V) (Unavaliable)\n\nAdditional Tools:\n[5] Show CPU information (Limited)\n[6] Exit")
    while True:
        try:
            select = int(input("Enter an option: "))
            if select == 1:
                clear_screen()
                select_raspberry_pi_board()
                break
            elif select == 5:
                clear_screen()
                cpu_information()
                break
            elif select == 6:
                clear_screen()
                sys.exit()
            else:
                print("Please select a valid option.")
        except ValueError:
            pass

def select_raspberry_pi_board(): #Raspberry Pi SBC selected. Will prompt for board number
    print("Select Raspberry Pi board:")
    print("[1] Raspberry Pi 5")
    print("[2] Raspberry Pi 4B")
    print("[3] Raspberry Pi 3A+ (Unavaliable)")
    print("[4] Raspberry Pi 3B+ (Unavaliable)")
    print("[5] Raspberry Pi 3B (Unavaliable)")

    while True:
        try:
            board_select = int(input("Enter an option: "))
            if board_select == 1:
                        clear_screen()
                        select_raspberry_pi5_overclock()
            elif board_select == 2:
                        clear_screen()
                        select_raspberry_pi4b_overclock()
            else:
                print("Please select a valid option.")
        except ValueError:
            pass

def select_raspberry_pi5_overclock(): #Raspberry Pi 5 board selected. Will prompt for OC settings
    print("Select {BOLD}Raspberry Pi 5 {RESET}overclock settings:")
    print("[1] Stable")
    print("[2] Medium")
    print("[3] Extreme (unstable)")
    pi5_overclock = int(input("Enter an option: "))

    if pi5_overclock == 1:
                clear_screen()
                confirm_overclock = str(input("Are you sure you want to overclock? [y/n]: "))
                if confirm_overclock.lower() == 'y':  
                    selected_overclock = "\narm_freq=2800\ngpu_freq=900"
                    raspberry_pi_4b_overclock()
                    clear_screen()
                    reboot = str(input("Overclock has been applied! Would you like to reboot now? [y/n]: "))
                    if reboot.lower() == 'y':
                        clear_screen()
                        print("Rebooting...")
                        os.system('reboot')
                    else:
                        clear_screen
                        print("Exiting...")
                        sys.exit()
                else:
                     clear_screen()
                     select_raspberry_pi5_overclock()

    if pi5_overclock == 2:
                clear_screen()
                confirm_overclock = str(input("Using this configuration forces turbo. This voids your warranty with Raspberry Pi. Are you sure you want to overclock? [y/n]: "))
                if confirm_overclock.lower() == 'y':  
                    selected_overclock = "\narm_freq=3000\ngpu_freq=900\nforce_turbo=1\nover_voltage_delta=50000"
                    raspberry_pi_4b_overclock()
                    clear_screen()
                    reboot = str(input("Overclock has been applied! Would you like to reboot now? [y/n]: "))
                    if reboot.lower() == 'y':
                        clear_screen()
                        print("Rebooting...")
                        os.system('reboot')
                    else:
                        clear_screen
                        print("Exiting...")
                        sys.exit()
                else:
                     clear_screen()
                     select_raspberry_pi5_overclock()

    if pi5_overclock == 3:
                clear_screen()
                confirm_overclock = str(input("Using this configuration forces turbo. This voids your warranty with Raspberry Pi. Are you sure you want to overclock? [y/n]: "))
                if confirm_overclock.lower() == 'y':  
                    selected_overclock = "\narm_freq=3100\ngpu_freq=900\nforce_turbo=1\nover_voltage_delta=50000"
                    raspberry_pi_4b_overclock()
                    clear_screen()
                    reboot = str(input("Overclock has been applied! Would you like to reboot now? [y/n]: "))
                    if reboot.lower() == 'y':
                        clear_screen()
                        print("Rebooting...")
                        # os.system('reboot')
                    else:
                        clear_screen
                        print("Exiting...")
                        sys.exit()
                else:
                     clear_screen()
                     select_raspberry_pi4b_overclock()

def select_raspberry_pi4b_overclock(): #Raspberry Pi 4b board selected. Will prompt for OC settings
    global selected_overclock #Makes selected_overclock global

    print(f"Select {BOLD}Raspberry Pi 4B {RESET}overclock settings:")
    print("[1] Stable")
    print("[2] Medium")
    print("[3] Extreme (unstable)")
    print("[4] Reset to defaults")
    pi4b_overclock = int(input("Enter an option: "))

    if pi4b_overclock == 1:
                clear_screen()
                confirm_overclock = str(input("Are you sure you want to overclock? [y/n]: "))
                if confirm_overclock.lower() == 'y':  
                    selected_overclock = "\narm_freq=2100\ngpu_freq=750\nover_voltage=6\nforce_turbo=1"
                    raspberry_pi_4b_overclock()
                    clear_screen()
                    reboot = str(input("Overclock has been applied! Would you like to reboot now? [y/n]: "))
                    if reboot.lower() == 'y':
                        clear_screen()
                        print("Rebooting...")
                        os.system('reboot')
                    else:
                        clear_screen
                        print("Exiting...")
                        sys.exit()
                else:
                     clear_screen()
                     select_raspberry_pi4b_overclock()

    if pi4b_overclock == 2:
                clear_screen()
                confirm_overclock = str(input("Using this configuration forces turbo. This voids your warranty with Raspberry Pi. Are you sure you want to overclock? [y/n]: "))
                if confirm_overclock.lower() == 'y':  
                    selected_overclock = "\narm_freq=2300\ngpu_freq=750\ngpu_mem=32\nover_voltage=14\nforce_turbo=1"
                    raspberry_pi_4b_overclock()
                    clear_screen()
                    reboot = str(input("Overclock has been applied! Would you like to reboot now? [y/n]: "))
                    if reboot.lower() == 'y':
                        clear_screen()
                        print("Rebooting...")
                        os.system('reboot')
                    else:
                        clear_screen
                        print("Exiting...")
                        sys.exit()
                else:
                     clear_screen()
                     select_raspberry_pi4b_overclock()

    if pi4b_overclock == 3:
                clear_screen()
                confirm_overclock = str(input("Using this configuration forces turbo. This voids your warranty with Raspberry Pi. Are you sure you want to overclock? [y/n]: "))
                if confirm_overclock.lower() == 'y':  
                    selected_overclock = "\ninitial_turbo=60\nover_voltage=15\narm_freq_min=100\narm_freq=2350\ngpu_freq=800\ngpu_mem=512"
                    raspberry_pi_4b_overclock()
                    clear_screen()
                    reboot = str(input("Overclock has been applied! Would you like to reboot now? [y/n]: "))
                    if reboot.lower() == 'y':
                        clear_screen()
                        print("Rebooting...")
                        os.system('reboot')
                    else:
                        clear_screen
                        print("Exiting...")
                        sys.exit()
                else:
                     clear_screen()
                     select_raspberry_pi4b_overclock()
            
    if pi4b_overclock == 4:
                clear_screen()
                confirm_overclock = str(input("Are you sure you want to reset to defaults [y/n]: "))
                if confirm_overclock.lower() == 'y':  
                    selected_overclock = ""
                    raspberry_pi_4b_overclock()
                    clear_screen()
                    reboot = str(input("Defaults have been restored. Would you like to reboot now? [y/n]: "))
                    if reboot.lower() == 'y':
                        clear_screen()
                        print("Rebooting...")
                        os.system('reboot')
                    else:
                        clear_screen
                        print("Exiting...")
                        sys.exit()
                else:
                     clear_screen()
                     select_raspberry_pi4b_overclock()

def raspberry_pi_4b_overclock(): #Writes to config.txt
    filename = '/boot/firmware/config.txt'
    
    # List of keywords to delete lines containing them
    keywords = [
        'arm_freq', 'gpu_freq', 'force_turbo', 'over_voltage', 
        'core_freq', 'sdram_freq', 'sdram_schmoo', 'over_voltage_sdram', 'initial_turbo', 'over_voltage_delta'
    ]
    
    # Read the current content of the file
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []
    
    # Filter out lines containing any of the keywords
    filtered_lines = [
        line for line in lines 
        if not any(keyword in line for keyword in keywords)
    ]
    
    # Remove empty lines after the last non-empty line
    i = len(filtered_lines) - 1
    while i >= 0 and not filtered_lines[i].strip():
        i -= 1
    
    # Only keep lines up to the last non-empty line
    filtered_lines = filtered_lines[:i + 1]
    
    # Write the filtered content back to the file
    with open(filename, 'w') as file:
        file.writelines(filtered_lines)
    
    # Append 'hello world' at the end of the file
    with open(filename, 'a') as file:
        file.write(str(selected_overclock))

def cpu_information():

    import psutil

    physical_cores = psutil.cpu_count(logical=False)
    total_threads = psutil.cpu_count(logical=True)

    try:
        freq = psutil.cpu_freq()
        if freq is not None:
            print(f"Number of physical cores: {physical_cores}")
            print(f"Number of logical CPUs (threads): {total_threads}")
            print(f"Maximum CPU frequency: {freq.max} MHz")
            print(f"Minimum CPU frequency: {freq.min} MHz")
            while True:
                print(f"\rCurrent CPU frequency: {freq.current} MHz (NOT CURRENTLY WORKING)", end='', flush=True)
                time.sleep(1)
        else:
            print("Unable to retrieve CPU frequency. It might not be supported.\n")
    except AttributeError as e:
        pass

if __name__ == "__main__":
    def check_package(package_name):
        return importlib.util.find_spec(package_name) is not None

    def install_package(package_name):
        subprocess.check_call(['apt', 'install', '-y', package_name])

    python_packages = {
        'colorama': 'python3-colorama',
        'pyfiglet': 'python3-pyfiglet',
        'psutil': 'python3-psutil'
    }

    if is_running_as_root():
            all_installed = True
            missing_packages = [pkg for pkg, pkg_name in python_packages.items() if not check_package(pkg)]
            
            if missing_packages:
                all_installed = False
                print(f"The following packages are missing: {', '.join(missing_packages)}")
                response = input("Do you want to install all missing packages? [y/n]: ").strip().lower()
                if response == 'y':
                    for package in missing_packages:
                        install_package(python_packages[package])
                    print("Installation complete.")
                    clear_screen()
                    select_sbc()
                else:
                    print("Missing packages will not be installed.")
            else:
                print("All required packages are already installed.")

            if all_installed:
                clear_screen()
                select_sbc()
    else:
        print("Oops! Please run the script again with sudo... exiting...")