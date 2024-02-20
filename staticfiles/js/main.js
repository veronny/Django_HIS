const getOptionChart = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/get_chart/");
        return await response.json();
    } catch (ex) {
        alert(ex.message);
    }
};

const initChart = async () => {
    const myChart = echarts.init(document.getElementById("chart"));
        
    myChart.setOption(await getOptionChart());

    myChart.resize();
};

window.addEventListener("load", async () => {
    await initChart();
});