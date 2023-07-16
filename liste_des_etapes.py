liste_des_etapes = (
    # pin_à_vérifier, question, Frequences,nouveau temps
    (1, ["En attente du démarrage de la bombe"], 3600, None),
    (2, ["Cher mOrtels, bienvenUe, ProfitEZ de vos derniers",]*4 +
        ["souffLEs",]*4 +
        ["à moins que vous ne soyez à la hauteuR de mOn merveilleUx GéniE",]*4 +
        ['tic tac',], 1.25, 10800),  # ROUGE
    (3, ["À saveur de fraise, il a de plus par rapport au Popsicle® ce que le Revello® a de plus par rapport au Fudge®"],
     0.95, None),  # Rouge/BLANC
    (4, ["Il était temps, c'était long!"] + ["NUM 10;1;21;14;5"]*6, 0.4, None),  # Jaune
    (5, ["Le temps passe vite quand on s'ammuse! Trouvez-vous? J'espère que vous vous amusez autant que moi.",
         "Il faut en profiter, rappelez-vous de ce qui vient au bout du tic tac...",
         "En voici une autre pour vous:",
         "Espace _____",
         "_____ de mémoire",
         "_____ d'oeuf",], 0.5, None),  # BLANC
    (6, ["Le vers blanc coupe la feuille verte.",], 1.2, None),  # VERT/BLANC
    (7, ["Les robots du futur seront-ils nus ou auront-ils une peau de plastique?"],
     1, None),  # Sans gaine
    (8, ["Mercenaire!", "armez", "uniquement",
     "vos", "ennemis!"], 1, None),  # MAUVE
    (9, ["Gandalf le ____"], 1, None),  # GRIS
    (10, ["Dring, dring",] + ["8^3 3^2 7^3 8^1"]*3, 0.5, None),  # VERT
    (11, ["Pièce de 1 sous"], 0.5, None),  # BRUN
    (12, ["Le ciel d'été parsemé de beaux cumulus blancs",], 3, None),  # BLEU/BLANC
    (13, ["""Le katana serait l'âme de ce guerrier japonais.""",] +
     ["1,1;3,3;2,0;5,0",]*4, 3, None),  # BLEU
    (14, ["EGNARO. Sachez jeunes naifs qu'il n'y aura pas de retour en arriere.",
          "Une fois que nous aurons remplis nos merveilleux desseins.",
          "Pour cette humanité qui nous appartiendra.",
          "Nous en serons les maitres pour l'éternité.",
          "Vous serez nos esclaves pour toujours.",
          "Désolé, j'oubliais."
          "Vous ne vivrez pas pour voir cette superbe époque.",], 0.5, None),  # ORANGE
    (15, ["Vous saurez bientôt s'il y en a au bout du tunnel.",
     "Et s'il n'y en avait pas?"], 1, None),  # Noir
    (16, ["e = >  ;  l = $  ;  o = ) ;  r = @",
          "b = a ; u = %  ;  i = +",
          "a = &  ;  t = ?  ;  n = *",] +
     ["&$>%   >?   *)+@"]*2, 0.75, None),  # Bleu et noir

    (17, ["Un beau légume racine longiligne croquant doté d'un feuillage au goût de celeri. Selon la croyance populaire, les léporidés rafoleraient de ce légume.",]*4 +
     ["tic tac"], 1, None),  # Orange et vert

    (18, ["N'essayez pas le piano, c'est trop compliqué pour vous, ça vous fera saigner du nez."]*8 + \
     ["Vous pouvez toujours l'essayer, ça ferait un beau mix de couleur..."]*2, 1, None),  # Blanc noir et rouge
    (19, ["Heureusement, il y a des gens qui ne saignent pas du nez lorsqu'ils joussent du piano."],
     1, None),  # Blanc et noir
    (20, ["Une facile en échange de vous verrez bien quoi...",]*3 +
     ["Le fil vert avec des taches noires et blanches"]*20, 1, None),  # VERT blanc noir
    (21, ["Ma couleur dominante est celle d'une patate qui partage certaines caractéristiques d'un chaton."]*2 +
     ["Ma couleur tachetée est à l'extrémité de la plus longue longueur d'onde du spectre visible."]*2 +
     ["Mon tout est un fil à couper si tu ne l'aurais pas deviné."]*2 +
     ["Petit indice, la caractéristique ce n'est pas d'être mignon.",
      "As tu déjà vu une patate mignonne?",
      "Tu as le droit de trouver les patates mignonnes, mais ce n'est pas de l'avis général."], 1, 300),
    (22, ["Je suis trop gentil, ça compte pour une bonne action je suppose.",
          "Ou peut être trois bonnes actions colorées.",] +
     ["J'exagère un peu ok, colorées et en noir et blanc"]*5, 0.7, 200),  # ROUGE noir, blanc
    (26, ["C'est une bombe!!!!",
          "Badaboom.",
          "boom",
          "Bada.",
          "boom",
          "C'est une bombe",
          "Avais tu oublié!",
          "Tic tac",
          "Qu'est ce que tu attend?",] +
     ["COUPE TOUT CE QUI RESTE!!!!!"]*5, 0.3, None),  # Ce qui reste (vert et noir)
    (None, [""], 3600, 0),
)
