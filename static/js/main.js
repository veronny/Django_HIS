const getOptionChart = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/get_chart/");
        return await response.json();
    } catch (ex) {
        alert(ex.message);
    }
};
// Grafico Ranking Redes
const getOptionChartRanking = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/get_chart_ranking/");
        return await response.json();
    } catch (ex) {
        alert(ex.message);
    }
};//

const initChart = async () => {
    const myChart = echarts.init(document.getElementById("chart"));
    const myChartRanking = echarts.init(document.getElementById("chart_ranking"));
    
    myChart.setOption(await getOptionChart());
    myChartRanking.setOption(await getOptionChartRanking());

    myChart.resize();
    myChartRanking.resize();
};

window.addEventListener("load", async () => {
    await initChart();
});


// Grafico Ranking Redes
//const getOptionChartRanking = async () => {
//    try {
//        const response = await fetch("http://127.0.0.1:8000/get_chart_ranking/");
//        return await response.json();
//    } catch (ex) {
//        alert(ex.message);
//    }
//};//

//const initChartRanking = async () => {
//    const myChartRanking = echarts.init(document.getElementById("chart_ranking"));//

//      myChartRanking.setOption(await getOptionChartRanking());
//      
//      myChartRanking.resize();
//};
//// escucha 
//window.addEventListener("load", async () => {
//    await initChartRanking();
//});