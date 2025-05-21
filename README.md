# Project_Data_Strukt

Projekta mērķis :
Izveidot programmu, kura nolasa ziņas no dažādiem ziņu portāliem, ka arī ļauj lietotājam izvēlēties visspiemērotāku 
kategoriju lasīšanai un ja viņš apmaldījās, tad varēs izsekot savai skatīšanas vēsturei un atrast mēklēto rakstu.

Projekta uzdevumi:
1. Iegūt datus no izvēlēta ziņu portāla ar Web scrapping palīdzību.
2. Saglabāt un uzglabāt iegūtos datus CSV failā.
3. Izveidot funkciju kurā notiks datu filtrešana pēc kategorijas.
4. Lietojot tādu datu struktūru kā stack, glabāt tajā skatīšanas vēsturi.
5. Beigās parādīt lietotājam viņa skatīšanas vēsturi.

Projekta veidošanas laikā tika izmantotas tādas bibliotēkas kā:
csv, requests, Beautifulsoup (paņemta no bs4)
csv bibliotēka ir ļoti svarīga bibliotēka, kuru jāizmnato strādājot ar failiem , lai nolasītu informāciju no faila un uzrakstīt informāciju tajā.
Beautifulsoup bibliotēka ir nepieciešama, lai strādātu ar HTML failiem. Tā arī ir nepieciešama bibliotēka Web scarppingam.
requests bibliotēka ir vajadzīga, lai piekļūtu tīmekļa vietnēm un iegūt HTML faila saturu.

Programmatūras izmantošanas metodes (soli pa solim)
1.solis - Programmas palaišana
2.solis - Ziņu apskatīšana pēc kategorijas
3.solis - Skatīšanas vēstures izvade
4.solis - Iziešana no programmas
