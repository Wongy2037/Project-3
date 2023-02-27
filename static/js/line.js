// import * as echarts from 'echarts';

var chartDom = document.getElementById('line');
var myChart = echarts.init(chartDom);
var option;

function createLine(xdata, ydata1,ydata2,ydata3) {
    option = {
        legend: {
            data: ['confirmed', 'deaths', 'recovered']
        },
        xAxis: {
            type: 'category',
            data: xdata,
        },
        yAxis: {
            type: 'value'
        },
           tooltip: {
      trigger: 'axis'
    },
        series: [
            {
                name: 'confirmed',
                data: ydata1,
                type: 'line'
            }, {
                name: 'deaths',
                data: ydata2,
                type: 'line'
            }, {
                name: 'recovered',
                data: ydata3,
                type: 'line'
            }
        ]
    };
    myChart.setOption(option);
}
