if answ == "y":
    console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{CHANNEL_USERNAME}[/bold blue].")
else:
    continue
else:
    console.print("[bold red]FAILED.[/bold red]")
    console.print("[bold yellow][!] Please try again.[/bold yellow]")
    sleep(2)
    continue

elif service == 17: # Unlimited Fuel
    console.print("[bold cyan][%] Unlocking Unlimited Fuel[/bold cyan]: ", end=None)
    if MUNAR_CPM_TOOL.unlimited_fuel():
        console.print("[bold green]SUCCESSFUL.[/bold green]")
        console.print("==================================")
        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
        if answ == "y":
            console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{CHANNEL_USERNAME}[/bold blue].")
        else:
            continue
    else:
        console.print("[bold red]FAILED.[/bold red]")
        console.print("[bold yellow][!] Please try again.[/bold yellow]")
        sleep(2)
        continue

elif service == 18: # Unlock House 3
    console.print("[bold cyan][%] Unlocking House 3[/bold cyan]: ", end=None)
    if MUNAR_CPM_TOOL.unlock_houses():
        console.print("[bold green]SUCCESSFUL.[/bold green]")
        console.print("==================================")
        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
        if answ == "y":
            console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{CHANNEL_USERNAME}[/bold blue].")
        else:
            continue
    else:
        console.print("[bold red]FAILED.[/bold red]")
        console.print("[bold yellow][!] Please try again.[/bold yellow]")
        sleep(2)
        continue

elif service == 19: # Unlock Smoke
    console.print("[bold cyan][%] Unlocking Smoke[/bold cyan]: ", end=None)
    if MUNAR_CPM_TOOL.unlock_smoke():
        console.print("[bold green]SUCCESSFUL.[/bold green]")
        console.print("==================================")
        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
        if answ == "y":
            console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{CHANNEL_USERNAME}[/bold blue].")
        else:
            continue
    else:
        console.print("[bold red]FAILED.[/bold red]")
        console.print("[bold yellow][!] Please try again.[/bold yellow]")
        sleep(2)
        continue

elif service == 20: # Change Races Wins
    console.print("[bold cyan][!] Insert how much races you win.[/bold cyan]")
    amount = IntPrompt.ask("[bold][?] Amount[/bold]")
    console.print("[bold cyan][%] Changing your data[/bold cyan]: ", end=None)
    if amount > 0 and amount <= 999999999999999999999999999:
        if MUNAR_CPM_TOOL.set_player_wins(amount):
            console.print("[bold green]SUCCESSFUL.[/bold green]")
            console.print("==================================")
            answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
            if answ == "y":
                console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{CHANNEL_USERNAME}[/bold blue].")
            else:
                continue
        else:
            console.print("[bold red]FAILED.[/bold red]")
            console.print("[bold yellow][!] Please try again.[/bold yellow]")
            sleep(2)
            continue
    else:
        console.print("[bold red]FAILED.[/bold red]")
        console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
        sleep(2)
        continue

elif service == 21: # Change Races Loses
    console.print("[bold cyan][!] Insert how much races you lose.[/bold cyan]")
    amount = IntPrompt.ask("[bold][?] Amount[/bold]")
    console.print("[bold cyan][%] Changing your data[/bold cyan]: ", end=None)
    if amount > 0 and amount <= 999999999999999999999:
        if MUNAR_CPM_TOOL.set_player_loses(amount):
            console.print("[bold green]SUCCESSFUL.[/bold green]")
            console.print("==================================")
            answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
            if answ == "y":
                console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{CHANNEL_USERNAME}[/bold blue].")
            else:
                continue
        else:
            console.print("[bold red]FAILED.[/bold red]")
            console.print("[bold yellow][!] Please try again.[/bold yellow]")
            sleep(2)
            continue
    else:
        console.print("[bold red]FAILED.[/bold red]")
        console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
        sleep(2)
        continue

elif service == 22: # Clone Account
    console.print("[bold cyan]Please Enter Account Detalis[/bold cyan]:")
    to_email = prompt_valid_value("[bold][?] Account Email[/bold]", "Email", password=False)
    to_password = prompt_valid_value("[bold][?] Account Password[/bold]", "Password", password=False)
    console.print("[bold cyan][%] Cloning your account[/bold cyan]: ", end=None)
    if MUNAR_CPM_TOOL.account_clone(to_email, to_password):
        console.print("[bold green]SUCCESSFUL.[/bold green]")
        console.print("==================================")
        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
        if answ == "y":
            console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{CHANNEL_USERNAME}[/bold blue].")
        else:
            continue
    else:
        console.print("[bold red]FAILED.[/bold red]")
        console.print("[bold yellow][!] Please try again.[/bold yellow]")
        sleep(2)
        continue

else:
    continue
break
break
