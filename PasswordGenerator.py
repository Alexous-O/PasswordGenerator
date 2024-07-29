import random

print(colored("""
_______    .-------.     .-./`)  .-./`)  .-./`)      ,-----.         _______    .---.  .---.      .-''-.       .-''-.   
\  ____  \  |  _ _   \    \ .-.') \ .-.') \ .-.')   .'  .-,  '.      /   __  \   |   |  |_ _|    .'_ _   \    .'_ _   \  
| |    \ |  | ( ' )  |    / `-' \ / `-' \ / `-' \  / ,-.|  \ _ \    | ,_/  \__)  |   |  ( ' )   / ( ` )   '  / ( ` )   ' 
| |____/ /  |(_ o _) /     `-'`"`  `-'`"`  `-'`"` ;  \  '_ /  | : ,-./  )        |   '-(_{;}_) . (_ o _)  | . (_ o _)  | 
|   _ _ '.  | (_,_).' __   .---.   .---.   .---.  |  _`,/ \ _/  | \  '_ '`)      |      (_,_)  |  (_,_)___| |  (_,_)___| 
|  ( ' )  \ |  |\ \  |  |  |   |   |   |   |   |  : (  '\_/ \   ;  > (_)  )  __  | _ _--.   |  '  \   .---. '  \   .---. 
| (_{;}_) | |  | \ `'   /  |   |   |   |   |   |   \ `"/  \  ) /  (  .  .-'_/  ) |( ' ) |   |   \  `-'    /  \  `-'    / 
|  (_,_)  / |  |  \    /   |   |   |   |   |   |    '. \_/``".'    `-'`-'     /  (_{;}_)|   |    \       /    \       /  
/_______.'  ''-'   `'-'    '---'   '---'   '---'      '-----'        `._____.'   '(_,_) '---'     `'-..-'      `'-..-'   
                                                                                                                         """, 'green'))
print("Automatic password generator")

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

passwordLength = int(input("How long would you like your password to be? "))

newPassword = []
for x in range(passwordLength):

    newPassword.append(random.choice(characters))

finalPassword = ''.join(map(str, newPassword))

print("\n This is your password: ", finalPassword)