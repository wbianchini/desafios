# Crawlers
	O crawler se encontra no package code. Existe uma classe RedditCrawler que define as regras a serem buscadas em uma página de thread. 

	Cada post possui uma classe 'scrollerItem' e a quantidade de upvotes só é encontrada em uma div irmã do botão de upvotes (única maneira de identificar). 

    Como entrada aceita uma lista contendo os sub reddits a serem lidos (como exemplo "cats;brazil;pugs")

    Devolve uma mensagem com a lista dos reddits que possuem cinco mil ou mais upvotes em uma lista

# Telegram Bot
    Os scripts para servir o bot ficam em ../bot, precisa apenas executar a pasta com "python3 bot" e a interação com o bot começa. Para fins de teste, deixei uma apikey de um bot existente sob o nome de @NadaPraFazerBot. 