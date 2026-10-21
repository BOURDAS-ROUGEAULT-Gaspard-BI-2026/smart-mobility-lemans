**Reflection 2.** Before reading the workflow steps later in this document: the static feed will run on a monthly schedule, the real-time feed every 15 minutes. Both could technically run every 15 minutes. Write your own guess now for why the static one doesn't.
 
Le static feed n'a pas besoin d'être lancé toutes les 15min car il ne subit probablement que très peu de modifications journalières ou même hebdomadaires. De plus, le traitement du pipeline est sûrement assez lourd et le relancer souvent consommerait beaucoup de ressources réseau. 

**Reflection 3.** Before running anything: if a tool infers each file's column types automatically and independently (so one file's stop_id column becomes numbers, another file's stop_id column stays text, just because of what values happened to appear in each file), what goes wrong when you try to join those two files on stop_id? Write your prediction, then compare it to the comment in the script below explaining why every GTFS file is read with dtype=str.

Si un outil déduit les types automatiquement, un fichier contenant uniquement des identifiants chiffrés sera converti en entiers, tandis qu'un autre fichier contenant aussi des identifiants alphanumériques sera lu comme du texte. Lors de la jointure sur stop_id, la comparaison entre un entier 1001 et une chaîne "1001" échouera.
