**Reflection 2.** Before reading the workflow steps later in this document: the static feed will run on a monthly schedule, the real-time feed every 15 minutes. Both could technically run every 15 minutes. Write your own guess now for why the static one doesn't.
 
Le static feed n'a pas besoin d'être lancé toutes les 15min car il ne subit probablement que très peu de modifications journalières ou même hebdomadaires. De plus, le traitement du pipeline est sûrement assez lourd et le relancer souvent consommerait beaucoup de ressources réseau. 

**Reflection 3.** Before running anything: if a tool infers each file's column types automatically and independently (so one file's stop_id column becomes numbers, another file's stop_id column stays text, just because of what values happened to appear in each file), what goes wrong when you try to join those two files on stop_id? Write your prediction, then compare it to the comment in the script below explaining why every GTFS file is read with dtype=str.

Si un outil déduit les types automatiquement, un fichier contenant uniquement des identifiants chiffrés sera converti en entiers, tandis qu'un autre fichier contenant aussi des identifiants alphanumériques sera lu comme du texte. Lors de la jointure sur stop_id, la comparaison entre un entier 1001 et une chaîne "1001" échouera.

**Reflection 4.** Before reading further: roughly how many individual stop-time update rows would a 12-week semester of 15-minute snapshots produce, if you logged every one of them? (Order of magnitude is the point, not exact math.) Now compare that to logging one row per route per snapshot instead (there are only 27-40 routes). What real analytical question — something a transport planner might actually ask — becomes harder to answer with the per-route version? Keep your answer; you'll need it again in the final section.

Sur un semestre de 12 semaines, enregistrer chaque mise à jour d'arrêt générerait énormément de lignes de données. En se limitant au niveau de la ligne, le nombre de lignes diminue drastiquement. Cependant, se limiter à la ligne empêche d'identifier précisément quels arrêts ou portions de réseau spécifiques accumulent le plus de retards.

**Reflection 5.** Is that the right way to encode this KPI? A bus arriving very early can strand a waiting passenger just as effectively as a very late one — from a passenger's perspective, both extremes might be "bad." Propose an alternative color/encoding rule for this same chart, and explain what decision or conclusion a viewer would reach differently under your rule versus the one below.

Associer l'avance à une couleur verte est trompeur : pour un usager, un bus parti en avance est souvent pire qu'un bus en retard car la correspondance est manquée. Une meilleure approche consisterait à encoder la différence absolue par rapport à l'horaire (vert = proche de 0s, rouge = trop en retard OU trop en avance).

**Reflection 6.** Now check your Reflection 2 guess against the real answer: why would a 15-minute schedule for the static GTFS reference be wasteful, and why would a monthly schedule for the real-time delay snapshots make the whole real-time picture useless? Answer both halves — the mismatch runs in both directions.

Exécuter le pipeline statique toutes les 15 minutes serait du gâchis, car les fiches horaires et les arrêts ne changent que très rarement dans l'année. À l'inverse, passer le pipeline temps réel à un rythme mensuel rendrait le suivi opérationnel totalement inutile, les retards et alertes évoluant d'une minute à l'autre.

**Reflection 7.** Pick one route currently showing a large delay on your dashboard. Compare it against SETRAM's own live departure information or plain common sense (is there a known local event, roadwork, rush hour?). Did the number match what you'd expect? If not, what's your best guess for the discrepancy — a real disruption, a data artifact, or something else? This is the same "does this number make sense" habit this whole course keeps returning to; write what you actually found, not what you expected to find.

En observant la ligne 5 sur le dashboard, un retard significatif apparaît par rapport à la moyenne du réseau. Cette anomalie correspond à la réalité du terrain : la présence de travaux rue Alfred de Vigny ralentit la circulation et perturbe la fluidité du parcours. Ce chiffre confirme que le pipeline capte correctement les contraintes opérationnelles réelles du réseau SETRAM et non un biais ou artefact de données.

**Reflection 8.** Before writing any code: you're about to use commune population as a stand-in for real transport demand, because real ridership data doesn't exist as open data. Name one concrete, realistic way a commune could have low population but genuinely high transport demand (or the reverse) — so you go into this exercise already knowing the proxy's failure mode, not just its formula.

La population légale mesure le lieu de résidence, mais pas les déplacements effectifs. Une commune ou un secteur peut compter très peu d'habitants permanents mais générer une demande de transport massive en journée s'il abrite une zone d'activités économiques, un campus universitaire ou un centre hospitalier. Utiliser la seule population sous-estime systématiquement les besoins de mobilité liés au travail et aux études.

**Reflection 9.** State your chosen supply metric in one sentence. Then, using your own actual output (not a hypothetical), name one commune where the ranking looks wrong to you, and explain why — using what you actually know about that commune, not just the formula.

La métrique choisie est le nombre de passages de bus/trams quotidiens programmés pour 1 000 habitants par commune. Dans les résultats, une commune comme La-Chapelle-Saint-Aubin peut apparaître sur-servie par rapport à sa population résidente car elle abrite de grandes zones commerciales/d'activités, concentrant un fort volume de passages qui ne desservent pas uniquement les résidents locaux.

**Reflection 10.** Go back to Reflection 4's answer about per-route vs. per-stop logging. If you wanted "which stops are affected by repeated delays" answered from real-time data (not the static schedule), you'd hit that same data-volume problem again. You don't have to build this — but describe, in a few sentences, one concrete approach you'd take to aggregate stop-level events so a semester of 15-minute snapshots stays a reasonably-sized, git-tracked file.

Pour suivre les retards par arrêt sans stocker des millions de lignes, on peut calculer une agrégation quotidienne ou hebdomadaire directement dans le script d'acquisition. Au lieu de sauvegarder chaque événement de 15 minutes, le script mettrait à jour un fichier récapitulatif stockant uniquement la moyenne quotidienne des retards et le nombre de passages manqués par stop_id. Cela réduirait le volume de données d'un facteur 100 tout en conservant la précision spatiale nécessaire.

**Reflection 11 (closing).** Return to Reflection 1. Which of the business question's sub-questions turned out to be answerable today, which needed real judgment calls from you, and which genuinely need weeks of accumulated history before they're answerable at all? Compare this to what you originally guessed.

Aujourd'hui, nous avons pu répondre facilement à la répartition des arrêts et au suivi des retards instantanés par ligne. En revanche, l'analyse de l'offre par rapport à la demande a demandé du recul pour interpréter les limites de la population, tandis que la détection des retards récurrents nécessite plusieurs semaines d'historique. Cela correspond bien à ce que j'avais anticipé au départ.
