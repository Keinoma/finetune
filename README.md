## Attention pr chaque fois :
- bien restart le kernel entre chaque entrainements


## Changements du 22.10.2026 :
Le but était de donner des réponses de capitales sous un certain format et qu'il répondes aux autres capitales sur lesquelles il s'est pas entrainé, dans me même format.

Q : Quelle est la capitale de la France ?
[RÉPONSE] Paris est la capitale de la France. — Fin de réponse. ; au lieu de "La capitale de la france est Paris."

Mais enft je lance l'entrainement, ~0.07% de params, la loss fait genre 3.39->1.07 à la bien.
Mais ensuite au test, le modèle avait pas asssez apris. Il répondait avec le nveau format pr les pays qui étaient dans le data.json, mais il avait pas appris à généraliser le format à ts les autres pays.

Ducoup il a fallu :
- + d'epochs :
        10epoch => 20 epochs .
- LoRA adapte sur ttes les couches liné :
        juste q_proj et v_proj => q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj. Ca fait ~0.5% param au lieu de 0.07% avt .
- changement dans le format :
        "conversation" (tjr dans le code mais commenté) => "prompt/completion"
        Mais j'ai isolé juste cette modif des autres (en testant les 2 formats genre) et ça semble avoir zéro impact.

   



