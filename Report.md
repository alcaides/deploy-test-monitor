# Stress Test  
>Reporte  

Se ejecuta un stress test con Locust para comprobar el rendimiento del sistema.  
  
>Sistema  

Hardware del servidor:  
Windows 10 64bits   
RAM: 8gb   
Procesador: i5 7200  
  
>Resultados

Se ensayaron simulaciones de 10, 30, 50, 100 y 300 usuarios, generados de a 1, 3, 5, 10 y 30 por segundo.  
Para 10 usuarios, se toleraron 12rps sin fallas. Hasta 100 usuarios no se registraron fallas, pero el tiempo de respuesta aumentó notablemente superando los 7 segundos para el módulo API y los 9 segundos para el módulo ML.  
Se procedió a escalar el módulo ML con 2 y 4 workers, pero en ambos casos la exigencia fue demasiada para los recursos del sistema. Como resultado, los tiempos de respuesta no sólo no mejroaron sino que empeoraron notablemente (x3 en algunos casos).  
  
 
![Locust Users](/assets/locust_users.png?raw=true)  
![Locust Response Time](/assets/locust_response_times.png?raw=true)  
![Locust Request per Second](/assets/locust_rps.png?raw=true)  
  
    
>Optimización  

El módulo ML es el que más tiempo de respuesta insume, y menos requests puede responder por minuto. Poder escalarlo, con un equipo de hardware superior, mejoraría el desemepeño general.  
Por otro lado, poder ofrecer una respuesta por API antes de tener los resultados del análisis de sentimiento mejoraría en cierto grado la experiencia del usuario.  


>Grafana  

Un dashboard de grafana permitirá monitorear el desempeño general del sistema. No se ejecutó en simultáneo con el scaling, pero se construyó un dashboard que ofrece lecturas de Request por Minuto y la cantidad de resultados Positivos y Negativos por Minuto.


![Dashboard](/assets/screen_grafana.png?raw=true)
