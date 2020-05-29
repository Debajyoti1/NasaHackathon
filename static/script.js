
        var getData = $.get('/popvsconf');
        getData.done(function(popvsconf){
            var ctx = document.getElementById('popvsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: popvsconf.population,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(255, 0, 30)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: popvsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {}
            });
        });
        var getData1 = $.get('/areavsconf');
        getData1.done(function(areavsconf){
            var ctx = document.getElementById('areavsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: areavsconf.area,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(89, 0, 255)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: areavsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {}
            });
        });
        var getData2 = $.get('/denvsconf');
        getData2.done(function(denvsconf){
            var ctx = document.getElementById('denvsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: denvsconf.density,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(9, 255, 0)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: denvsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {}
            });
        });

        var getData3 = $.get('/actvsconf');
        getData3.done(function(actvsconf){
            var ctx = document.getElementById('actvsconf').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                // The data for our dataset
                data: {
                    labels: actvsconf.active,
                    datasets: [{
                        label: 'Confirmed',
                        fill: false,
                        borderWidth: 1,
                        backgroundColor: 'rgb(0, 153, 255)',
                        borderColor: 'rgb(255, 255, 225)',
                        data: actvsconf.confirmed
                    }]
                },

                // Configuration options go here
                options: {}
            });
        });