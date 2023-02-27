var map = echarts.init(document.getElementById('line'));//Initial

var COLORS = ["#ffffff", "#faebd2", "#e9a188", "#d56355", "#bb3937", "#772526", "#480f10"];//Color
var dataList=[//Data
			    {name:"Other",value:0},
			    {name: 'Beijing', value: 97},
			    {name: 'Tianjin', value: 5},
			    {name: 'Shanghai', value: 30},
			    {name: 'Chongqing', value: 2},
			    {name: 'Hebei', value: 2},
			    {name: 'Henan', value: 1},
			    {name: 'Yunnan', value: 2},
			    {name: 'Liaoning', value: 4},
			    {name: 'Heilongjiang', value: 13},
			    {name: 'Hunan', value: 0},
			    {name: 'Anhui', value: 0},
			    {name: 'Shandong', value: 9},
			    {name: 'Xinjiang', value: 0},
			    {name: 'Jiangsu', value: 5},
			    {name: 'Zhejiang', value: 15},
			    {name: 'Jiangxi', value: 1},
			    {name: 'Hubei', value: 8685},
			    {name: 'Guengjsae', value: 3},
			    {name: 'Gansu', value: 40},
			    {name: 'Shanxi', value: 1},
			    {name: 'Inner_Mongolia', value: 1},
			    {name: 'Shaanxi', value: 7},
			    {name: 'Jilin', value: 0},
			    {name: 'Fujian', value: 0},
			    {name: 'Guizhou', value: 0},
			    {name: 'Guangdong', value: 49},
			    {name: 'Qinghai', value: 0},
			    {name: 'Tibet', value: 0},
			    {name: 'Sichuan', value: 17},
			    {name: 'Ningxia', value: 0},
			    {name: 'Hainan', value: 1},
			    {name: 'Taiwan', value: 54},
			    {name: 'Hong_Kong', value: 70},
			    {name: 'Macao', value: 2}
			]

	var option={

				tooltip: {
						formatter:function(params,ticket, callback){
							return params.seriesName+'<br />'+params.name+'：'+params.value
						}//inital data
					},
				backgroundColor:'#eeeeee',//background color
				visualMap: {//visualMap
					type: 'piecewise',
					orient: 'horizontal',

					left: 'left',
					top: 'bottom',

					pieces: [{
						value: 0, color: COLORS[0]
					}, {
						min: 1, max: 9, color: COLORS[1]
					}, {
						min: 10, max: 99, color: COLORS[2]
					}, {
						min: 100, max: 499, color: COLORS[3]
					}, {
						min: 500, max: 999, color: COLORS[4]
					}, {
						min: 1000, max: 10000, color: COLORS[5]
					}, {
						min: 10000, color: COLORS[6]
					}],
					inRange: {
						color:COLORS 
					},

					show:true
				},
				geo: {
					map: 'china',
					roam: false,
					zoom:1.23,
					label: {
						normal: {
							show: true,
							fontSize:'10',
							color: 'rgba(0,0,0,0.7)'
						}
					},
					itemStyle: {
						normal:{
							borderColor: 'rgba(0, 0, 0, 0.2)'
						},
						emphasis:{
							areaColor: '#F3B329',
							shadowOffsetX: 0,
							shadowOffsetY: 0,
							shadowBlur: 20,
							borderWidth: 0,
							shadowColor: 'rgba(0, 0, 0, 0.5)'
						}
					}
				},
				series : [
					{
						name: 'Information_content',
						type: 'map',
						geoIndex: 0,
						data:dataList
					}
				]
			}

			map.setOption(option);
