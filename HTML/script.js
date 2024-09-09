async function fetchOKXPrice(pair) {
    const response = await fetch(`https://www.okx.com/api/v5/market/ticker?instId=${pair}-SWAP`);
    if (!response.ok) {
        throw new Error(`Erro na API OKX: ${response.statusText}`);
    }
    const data = await response.json();
    return parseFloat(data.data[0].last);
}

async function fetchMercadoBitcoinPrice(pair) {
    const response = await fetch(`https://www.mercadobitcoin.net/api/${pair}/ticker/`);
    if (!response.ok) {
        throw new Error(`Erro na API Mercado Bitcoin: ${response.statusText}`);
    }
    const data = await response.json();
    return parseFloat(data.ticker.last);
}



async function monitorPrices() {
    const pairs = ["BTC-USDT", "ETH-USDT"]; // Adicione mais pares conforme necessário
    const priceTable = document.getElementById("prices").getElementsByTagName("tbody")[0];
    priceTable.innerHTML = "";

    for (const pair of pairs) {
        const okxPair = pair.replace("-", "");
        const mbPair = pair.toLowerCase();

        try {
            const [okxPrice, mbPrice] = await Promise.all([
                fetchOKXPrice(okxPair),
                fetchMercadoBitcoinPrice(mbPair)
            ]);

            // Calcular a diferença absoluta e percentual entre os preços
            const priceDifference = Math.abs(okxPrice - mbPrice);
            const percentageDifference = (priceDifference / okxPrice) * 100;

            // Determinar se há uma oportunidade de arbitragem
            const arbitrageOpportunity = percentageDifference > 0.5; // Exemplo: arbitragem se a diferença for maior que 0.5%

            const arbitrageClass = arbitrageOpportunity ? 'arbitrage' : 'no-arbitrage';
            const arbitrageText = arbitrageOpportunity ? 'Sim' : 'Não';

            const row = `
                <tr>
                    <td>${pair}</td>
                    <td>$${okxPrice.toFixed(2)}</td>
                    <td>$${mbPrice.toFixed(2)}</td>
                    <td class="${arbitrageClass}">${arbitrageText}</td>
                </tr>
            `;

            priceTable.innerHTML += row;
        } catch (error) {
            console.error(`Erro ao buscar preços para o par ${pair}:`, error);
            priceTable.innerHTML += `
                <tr>
                    <td colspan="4">Erro ao buscar preços para o par ${pair}: ${error.message}</td>
                </tr>
            `;
        }
    }
}

setInterval(monitorPrices, 30000); // Atualiza a cada 30 segundos
monitorPrices();


setInterval(monitorPrices, 30000); // Atualiza a cada 30 segundos
monitorPrices();