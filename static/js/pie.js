var chartpie = document.getElementById('pie');
var pieChart = echarts.init(chartpie);
var pieption;

function setPie(piedata) {
    pieption = {
        title: [{
            show: true,
            text: 'The fourth quarter of  the developments',
            subtext: 'Covid Data',
            left: 'center'
        }, {
            subtext: '2020-2021 the fourth quarter of \n the number of confirmed distribution ',
            left: '16.67%',
            top: '55%',
            textAlign: 'center'
        },
            {
                subtext: '2021-2022 the fourth quarter of\n the number of confirmed distribution ',
                left: '50%',
                top: '90%',
                textAlign: 'center'
            },
            {
                subtext: '2022-2023 the fourth quarter of\n the number of confirmed distribution ',
                left: '80%',
                top: '55%',
                textAlign: 'center'
            }],

        tooltip: {
            trigger: 'item'
        },
        legend: {
            orient: 'vertical',
            left: 'left'
        },
        series: [
            {
                name: '2020-2021',
                type: 'pie',
                center: ['20%', '40%'],
                radius: '30%',
                data: [
                    {value: piedata["1"], name: 'The First Quarter'},
                    {value: piedata["2"], name: 'The Second Quarter'},
                    {value: piedata["3"], name: 'The Third Quarter'},
                    {value: piedata["4"], name: 'The Forth Quarter'}
                ],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }, {
                name: '2021-2022',
                type: 'pie',
                radius: '30%',
                center: ['50%', '75%'],
                data: [
                    {value: piedata["5"], name: 'The First Quarter'},
                    {value: piedata["6"], name: 'The Second Quarter'},
                    {value: piedata["7"], name: 'The Third Quarter'},
                    {value: piedata["8"], name: 'The Forth Quarter'}
                ],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }, {
                name: '2022-2023',
                type: 'pie',
                radius: '30%',
                center: ['80%', '40%'],
                data: [
                    {value: piedata["9"], name: 'The First Quarter'},
                    {value: piedata["10"], name: 'The Second Quarter'},
                    {value: piedata["11"], name: 'The Third Quarter'},
                    {value: piedata["12"], name: 'The Forth Quarter'}
                ],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    }
    pieChart.setOption(pieption);
};
