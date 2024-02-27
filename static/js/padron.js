const getOptionChartPadron = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/padron_situacion/get_chart_padron_edades/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const getOptionChartPadronSexo = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/padron_situacion/get_chart_padron_sexo/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const getOptionChartPadronDNI = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/padron_situacion/get_chart_padron_dni/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const getOptionChartPadronSeguro = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/padron_situacion/get_chart_padron_seguro/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const getOptionChartPadronEncontrado = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/padron_situacion/get_chart_padron_encontrado/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const getOptionChartPadronVisitado = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/padron_situacion/get_chart_padron_visitado/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const getOptionChartPadronCelular = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/padron_situacion/get_chart_padron_celular/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const getOptionChartPadronFrecuencia = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/padron_situacion/get_chart_padron_frecuencia/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const getOptionChartPadronEntidad = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/padron_situacion/get_chart_padron_entidad/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const getOptionChartPadronAtencion = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/padron_situacion/get_chart_padron_atencion/");
        return await response.json();
    } catch (ex) {
        alert(ex);
    }
};

const initChartPadron = async () => {
    const myChartPadron = echarts.init(document.getElementById("chart_padron_edades"));
    const myChartPadronSexo = echarts.init(document.getElementById("chart_padron_sexo"));
    const myChartPadronDNI = echarts.init(document.getElementById("chart_padron_dni"));
    const myChartPadronSeguro = echarts.init(document.getElementById("chart_padron_seguro"));
    const myChartPadronEncontrado = echarts.init(document.getElementById("chart_padron_encontrado"));
    const myChartPadronVisitado = echarts.init(document.getElementById("chart_padron_visitado"));
    const myChartPadronCelular = echarts.init(document.getElementById("chart_padron_celular"));
    const myChartPadronFecuencia = echarts.init(document.getElementById("chart_padron_frecuencia"));
    const myChartPadronEntidad = echarts.init(document.getElementById("chart_padron_entidad"));
    const myChartPadronAtencion = echarts.init(document.getElementById("chart_padron_atencion"));

    myChartPadron.setOption(await getOptionChartPadron());
    myChartPadronSexo.setOption(await getOptionChartPadronSexo());
    myChartPadronDNI.setOption(await getOptionChartPadronDNI());
    myChartPadronSeguro.setOption(await getOptionChartPadronSeguro());
    myChartPadronEncontrado.setOption(await getOptionChartPadronEncontrado());
    myChartPadronVisitado.setOption(await getOptionChartPadronVisitado());
    myChartPadronCelular.setOption(await getOptionChartPadronCelular());
    myChartPadronFecuencia.setOption(await getOptionChartPadronFrecuencia());
    myChartPadronEntidad.setOption(await getOptionChartPadronEntidad());
    myChartPadronAtencion.setOption(await getOptionChartPadronAtencion());
  
    myChartPadron.resize();    
    myChartPadronSexo.resize();
    myChartPadronDNI.resize();   
    myChartPadronSeguro.resize();   
    myChartPadronEncontrado.resize();   
    myChartPadronVisitado.resize();   
    myChartPadronCelular.resize();
    myChartPadronFecuencia.resize();
    myChartPadronEntidad.resize();                          
    myChartPadronAtencion.resize();

};

window.addEventListener("load", async () => {
    await initChartPadron();
});