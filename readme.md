**Python Multi-threaded Port Scanner** 

Um scanner de portas TCP robusto e veloz desenvolvido em Python, utilizando concorrência para otimização de performance.

**🛠️ Funcionalidades**

    Scan TCP Multithread: Utiliza ThreadPoolExecutor para gerenciar conexões simultâneas.

    Banner Grabbing: Captura informações de serviços ativos nas portas abertas.

    Validação de Input: Proteção contra IPs inválidos usando a biblioteca ipaddress.

    Output Persistente: Salva automaticamente os resultados positivos em um arquivo .txt.

    Controle de Performance: Permite ao usuário definir o número de threads via CLI.

**🚀 Como usar**
 ```
python scanner.py -t 192.168.1.1 -p 20-443 --tcp --threads 100
