## PROJETO MONITOR-SENSORES TCP MULTI-THREAD

**FUNCIONAMENTO DO SISTEMA**

* O MONITOR é iniciado primeiro e escuta em uma porta FIXA   

* O SENSOR faz uma conexão com o MONITOR, e entra em um loop para aguardar comandos do MONITOR

* A função main do MONITOR acorda, cria uma THREAD dedicada para o SENSOR e volta a aguardar conexões

* A THREAD ouve dados de um único sensor, e dorme quando não há dados no buffer do SENSOR