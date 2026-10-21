**Reflection 2.** Before reading the workflow steps later in this document: the static feed will run on a monthly schedule, the real-time feed every 15 minutes. Both could technically run every 15 minutes. Write your own guess now for why the static one doesn't.
 
Le static feed n'a pas besoin d'être lancé toutes les 15min car il ne subit probablement que très peu de modifications journalières ou même hebdomadaires. De plus, le traitement du pipeline est sûrement assez lourd et le relancer souvent consommerait beaucoup de ressources réseau. 
