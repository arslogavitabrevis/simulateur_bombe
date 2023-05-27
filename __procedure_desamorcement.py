from machine import Pin, Timer
# from typing import Tuple, Optional

with open("logos_ascii/carotte.txt", 'r') as f:
    carotte = f.read()
liste_des_etapes = (
    # pin_à_vérifier, question, Frequences,nouveau temps
    (1, ["En attente du démarrage de la bombe"], 1, None),
    (2, ["bienvenue cher mortels profitez de vos dernier souffles",
         "à moins que vous ne soyez à la hauteur",
         "de mon merveilleUx génie",
         "bienvenue Cher mOrtels",
         "ProfitEz de vos dernieR souffLEs",
         "à moins que vous ne soyez à la hauteuR",
         "de mOn merveilleUx GéniE",
         'tic tac',], 1, None),  # ROUGE
    (3, ["À saveur d'orange, il est au Popsicle® ce que le Revello® est au Fudge®"],
     1, None),  # ORANGE/BLANC
    (4, ['Il était temps bande de poshes', "NUM 10;1;21;14;5"], 0.4, None),  # Jaune
    (5, ["Le temps passe vite quand on s'ammuse trouvez vous.",
         "J'espères que vous vous amusez autant que moi.",
         "Il faut en profitez, rapelez vous ce qui vient au bout du tic tac...",
         "En voici une autre pour vous:",
         "Espace _____",
         "_____ de mémoire",
         "____ d'oeuf",], 0.5, None),  # BLANC
    (6, ["""   
   |
 .'|'.
/.'|\ \
| /|'.|
 \ |\/
  \|/
   `""", """
                          (o)(o)
                          /     \
                         /       |
                        /   \  * |
          ________     /    /\__/
  _      /        \   /    /
 / \    /  ____    \_/    /
//\ \  /  /    \         /
V  \ \/  /      \       /
    \___/        \_____/
""",
         """"   
   |
 .'|'.
/.'|\ \    
_______    
| /|'.|
 \ |\/
  \|/
   `""",
         "Le vers blanc coupe la feuille verte.",], 1.2, None),  # VERT/BLANC
    (7, ["Les robot du futur seront-ils nu comme des vers ou auront ils une peau de PVC?"],
     1, None),  # Sans gaine
    (8, ["Mercenaire!", "armez", "uniquement",
     "vos", "ennemis!"], 1, None),  # MAUVE
    (9, ["Gandalf le ____"], 1, None),  # GRIS
    (10, ["Dring, dring", "8^3 3^2 7^3 8^1"], 0.5, None),  # VERT
    (11, ["Pièce de 1 sous"], 0.5, None),  # BRUN
    (12, ["""
                _                                  
              (`  ).                   _           
             (     ).              .:(`  )`.       
)           _(       '`.          :(   .    )      
        .=(`(      .   )     .--  `.  (    ) )      
       ((    (..__.:'-'   .+(   )   ` _`  ) )                 
`.     `(       ) )       (   .  )     (   )  ._   
  )      ` __.:'   )     (   (   ))     `-'.-(`  ) 
)  )  ( )       --'       `- __.'         :(      )) 
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'          
                                        
--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.,
""",
          "Le ciel d'été parsemé de beaux cumulus bleu",], 3, None),  # BLEU/BLANC
    (13, ["""
⠀⠀⠀⠀⠀⠀⠀⢸⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢠⡇⢀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⢸⡇⣼⢃⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⣸⠁⣿⣸⣿⡿⠀⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠐⣎⣿⣿⣰⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⢋⣶⣶⣶⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣶⣤⣤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡇⣿⣿⣿⠿⣛⣩⣭⣭⣭⣭⣉⣙⡛⣋⣩⣥⣴⣶⣶⣶⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠇⣾⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⣛⡛⠛⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠁⠚⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣡⣴⣾⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣏⣼⣿⣿⣿⣿⣿⣯⣍⣛⠿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⠏⢻⣿⣿⣿⣿⣿⣿⣿⠿⠛⢛⣛⠛⠻⠿⣷⣤⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣶⣷⣦⣝⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣍⣝⡛⠿⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢰⡿⣫⣿⣿⣿⡟⣿⣿⡇⢸⣿⣿⣿⣿⠿⢿⣿⣷⣦⣌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⣡⢾⣿⣿⣿⡟⣸⣿⣿⡇⢸⣿⣿⣿⣿⣿⣷⣦⣌⡙⠛⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⢋⣵⣿⣿⣿⣿⢡⣿⣿⣿⠃⢸⣿⣿⣿⣿⣤⣬⣙⡛⠿⢷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣶⣿⣿⣿⣿⣿⠇⣘⣩⣿⣿⠀⢸⣿⣿⣿⣿⡛⡻⠿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣵⣾⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣷⣦⣌⡙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠿⠟⠛⠻⢿⣿⣿⣿⣿⠀⢾⣿⣿⣿⣿⣴⣮⣍⡛⠻⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠿⠛⠉⣠⣴⣾⠟⣃⣤⠙⣿⣿⣿⡀⠻⠿⢿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⡿⢛⣩⣴⣿⣿⣿⣧⠘⣿⣿⣿⣶⣦⣤⣄⣀⣈⠉⠙⠻⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠙⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⡛⢁⣼⣿⣿⣿⡿⠟⣋⣵⣿⣿⡇⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣾⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼⡟⣿⣿⣿⣿⣿⡿⠟⣠⣿⣿⣿⣿⣿⣿⣿⣟⢻⡉⣛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠀⠈⠁⠉⠙⠉⠀⠀⠉⠉⠉⢛⠛⠛⠿⠿⠿⢠⢇⣿⣿⣿⣿⣿⣿⡿⢋⣉⣉⠛⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⣡⣴⣿⣿⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣭⣭⣿⣿⣿⣿⠿⢿⣿⣿⣿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⣿⣟⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠉⠙⠛⠿⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣙⣋⣭⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣿⣿⣿⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⡟⠰⠿⠿⠿⠿⠿⣿⢿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⢣⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⡿⢸⣿⣿⣿⣿⣿⡸⠿⠿⠿⢿⣿⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣷⣦⣀⠀
⠀⠀⠀⠀⠀⠀⣾⡏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⠧
⠀⠀⠀⠀⠀⠀⣿⡇⠾⢿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⠇⣶⣶⣶⣶⣶⣶⣦⣼⣿⣿⣿⡟⢠⣿⣿⣿⣿⣿⣿⣿⡇⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣥⣾⣿⣿⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⠿⠿⠿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢼⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
          "1,1;3,3;2,0;5,0",], 3, None),  # BLEU
    (14, ["EGNARO: Sachez jeunez naifs qu'il n'y aura pas de retour en arriere.",
          "Une fois que nous aurons remplis nos merveilleux dessin.",
          "Pour cette humanité qui nous appartiendra.",
          "Nous en seront les maitre pour l'éternité",
          "Vous serez nos eslaves pour toujours.",
          "Désolé, j'oubliais."
          "Vous ne vivrez pas pour voir cette superbe époque.",], 0.5, None),  # ORANGE
    (15, ["Vous saurez bientôt s'il y en a au bout du tunnel.",
     "Et s'il n'en avait pas?"], 1, None),  # Noir
    (16, ["e = > , l = $, o = ), r = @",
          "b = a , u = %,  i = +",
          "a = & , t = ?, n = *",
          "&$>% >? *)+@"], 0.75, None),  # Bleu et noir

    (17, [carotte, carotte, carotte, carotte,
          "Un beau légume racine fait sur le long croquant avec un feuillage au gout ce celeri.",
          carotte, carotte,
          "C'est long, tic tac"], 1, None),  # Orange et vert
    # Blanc noir et rouge
    (18, ["Vu votre niveau d'intelligence, n'essayez pas le piano c'est trop compliqué pour vous, ça vous fera saigner du nez."], 1, None),
    (19, ["Heureusement, il y a des gens qui ne saigne pas du nez lorsqu'ils en jousseent."], 1, None),
    (20, ["Une facile en échange de vous verrez bien quoi...",
     "Le vert avec des taches noires et blanches"], 1, None),  # VERT blanc noir
    (21, ["Ma couleur dominante est celle d'une patate qui partage certaine caractéristique d'un chaton.",
          "Ma couleur tacheté est à l'extrémité de plus longue longueur d'onde du spectre visible.",
          "Mon tout est un fil à couper si tu ne l'aurais pas deviné.",
          "Petit indice, la caractéristique ce n'est pas d'être mignon. As tu déjà vu une patate mignone?",
          "Tu as le droit de trouver les patates mignones, mais ce n'est pas de l'avis général."], 1, 300),
    (22, ["Je suis trop gentil, ça compte pour une bonne action je suppose.",
          "Ou peut être trois bonne action colorées.",
          "J'exagère un peu ok colorées et en noir et blanc"], 0.7, 200),  # ROUGE noir, blanc
    (23, ["C'est une bombe!!!!",
          "Badaboom.",
          "boom",
          "Bada.",
          "boom",
          "Badaboom.",
          "boom",
          "Bada.",
          "boom",
          "Avais tu oublié!",
          "Tic tac",
          "Tic tac",
          "Tic tac",
          "Avais tu oublié!",
          "Tic tac",
          "Qu'est ce que tu attend?",
          "COUPE TOUT!!!!!"], 0.3, None)  # Ce qui reste
)


class SequenceDesarmorcement:
    def __init__(self, fonction_mise_a_jour):

        # Variable globale pour l'étape
        self.__etape = 0

        self.__fct_mise_a_jour = fonction_mise_a_jour

        # Define the inputs pins
        self.__cable_coupes = 0
        self.__pins = [Pin(5, Pin.IN, Pin.PULL_DOWN)
                       for i in range(len(liste_des_etapes)+1)]
        for i, pin in enumerate(self.__pins):
            pin.irq(trigger=Pin.IRQ_FALLING,
                    handler=lambda pin, pin_num=i: self.__gpio_interrup_callback(pin, pin_num))

        # Initialiser la bombe à l'étape initiale
        self.__verification(update=True)

        # Faire une timer pour vérifier l'étape au secondes
        # au cas ou l'interrupt serait manqué
        self.__timer = Timer()
        self.__timer.init(
            period=1500, callback=self.__callback_timer_verification)

    def __gpio_interrup_callback(self, pin: Pin, pin_number: int):
        pin_mask = 1 << pin_number
        if not self.__cable_coupes & pin_mask:
            self.__cable_coupes |= pin_mask
            self.__etape += 1
            self.__verification(update=True)

    def __callback_timer_verification(self, timer: Timer):
        self.__verification()

    def __verification(self, update=False):
        (pin_a_verifier,
         question,
         periode,
         nouveau_temps) = liste_des_etapes[self.__etape]

        # Si la pin a vérifier a été coupé
        if self.__pins[pin_a_verifier].value() == False:
            print("pin {} déconnecté".format(pin_a_verifier))
            self.__etape += 1
            if self.__etape >= len(liste_des_etapes):
                self.__etape = len(liste_des_etapes)-1
                return
            self.__verification(update=True)
            return
        print("pin {} value: {}".format(pin_a_verifier,
              self.__pins[pin_a_verifier].value()))
        if update:
            self.__fct_mise_a_jour(question, periode, nouveau_temps)
