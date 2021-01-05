/*** First Chart in Dashboard page ***/

	$(document).ready(function() {
		var all_cnt = document.getElementById("all_cnt").value;
		var net_cnt = document.getElementById("net_cnt").value;
		var rate = (net_cnt / all_cnt)*100;
		rate = Math.round(rate);
		info = new Highcharts.Chart({
			chart: {
				renderTo: 'netflix',
				margin: [0, 0, 0, 0],
				backgroundColor: null,
                plotBackgroundColor: 'none',

			},

			title: {
				text: null
			},

			tooltip: {
				formatter: function() {
					return this.point.name +': '+ this.y +' %';

				}
			},
		    series: [
				{
				borderWidth: 2,
				borderColor: '#F1F3EB',
				shadow: false,
				type: 'pie',
				name: 'Income',
				innerSize: '65%',
				data: [
					{ name: '', y: rate, color: '#b231c8' },
					{ name: '', y: 100 - rate, color: '#3d3d3d' }
				],
				dataLabels: {
					enabled: false,
					color: '#000000',
					connectorColor: '#000000'
				}
			}]
		});

	});

	$(document).ready(function() {
		var all_cnt = document.getElementById("all_cnt").value;
		var hu_cnt = document.getElementById("hulu_cnt").value;
		var rate = (hu_cnt / all_cnt)*100;
		rate = Math.round(rate);
		info = new Highcharts.Chart({
			chart: {
				renderTo: 'hulu',
				margin: [0, 0, 0, 0],
				backgroundColor: null,
                plotBackgroundColor: 'none',

			},

			title: {
				text: null
			},

			tooltip: {
				formatter: function() {
					return this.point.name +': '+ this.y +' %';

				}
			},
		    series: [
				{
				borderWidth: 2,
				borderColor: '#F1F3EB',
				shadow: false,
				type: 'pie',
				name: 'Income',
				innerSize: '65%',
				data: [
					{ name: '', y: rate, color: '#b2c831' },
					{ name: '', y: 100 - rate, color: '#3d3d3d' }
				],
				dataLabels: {
					enabled: false,
					color: '#000000',
					connectorColor: '#000000'
				}
			}]
		});

	});
/*** second Chart in Dashboard page ***/

	$(document).ready(function() {
		var all_cnt = document.getElementById("all_cnt").value;
		var pv_cnt = document.getElementById("pv_cnt").value;
		var rate = (pv_cnt / all_cnt)*100;
		rate = Math.round(rate);
		info = new Highcharts.Chart({
			chart: {
				renderTo: 'space',
				margin: [0, 0, 0, 0],
				backgroundColor: null,
                plotBackgroundColor: 'none',

			},

			title: {
				text: null
			},

			tooltip: {
				formatter: function() {
					return this.point.name +': '+ this.y +' %';

				}
			},
		    series: [
				{
				borderWidth: 2,
				borderColor: '#F1F3EB',
				shadow: false,
				type: 'pie',
				name: 'SiteInfo',
				innerSize: '65%',
				data: [
					{ name: '', y: rate, color: '#fa1d2d' },
					{ name: '', y: 100-rate, color: '#3d3d3d' }
				],
				dataLabels: {
					enabled: false,
					color: '#000000',
					connectorColor: '#000000'
				}
			}]
		});

	});

	$(document).ready(function() {
		var all_cnt = document.getElementById("all_cnt").value;
		var dis_cnt = document.getElementById("dis_cnt").value;
		var rate = (dis_cnt / all_cnt)*100;
		rate = Math.round(rate);
		info = new Highcharts.Chart({
			chart: {
				renderTo: 'disney',
				margin: [0, 0, 0, 0],
				backgroundColor: null,
                plotBackgroundColor: 'none',

			},

			title: {
				text: null
			},

			tooltip: {
				formatter: function() {
					return this.point.name +': '+ this.y +' %';

				}
			},
		    series: [
				{
				borderWidth: 2,
				borderColor: '#F1F3EB',
				shadow: false,
				type: 'pie',
				name: 'Income',
				innerSize: '65%',
				data: [
					{ name: 'load percentage', y: rate, color: '#30c8b2' },
					{ name: 'rest', y: 100 - rate, color: '#3d3d3d' }
				],
				dataLabels: {
					enabled: false,
					color: '#000000',
					connectorColor: '#000000'
				}
			}]
		});

	});
