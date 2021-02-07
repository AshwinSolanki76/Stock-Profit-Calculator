// import yahoo-stock-api from "yahoo-stock-api"


const yahooStockAPI  = require('yahoo-stock-api');
async function main()  {
	const startDate = new Date('08/21/2020');
	const endDate = new Date('08/26/2020');
	console.log(await yahooStockAPI.getHistoricalPrices(startDate, endDate, 'AAPL', '1d'));
}
main();
