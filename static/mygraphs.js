var progressive = {
    type: 'line',
    data: {
        labels: ["10/21", "10/31", "11/1"],// x- axis label
        datasets: [{
            label: 'avg fantasy points',
            data: [12, 19, 3, 5, 2, 3],

            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
  
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',

            ],
            borderWidth: 1
        }]
    },
    options: {
        // maintainAspectRatio:false,
        responsive:true,
    }
}

var pergame = {
    type: 'bar',
    data: {
        labels: ["10/21", "10/31", "11/1"],// x- axis label
        datasets: [{
            label: 'avg fantasy points',
            data: [12, 19, 3, 5, 2, 3],

            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
  
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',

            ],
            borderWidth: 1
        }]
    },
    options: {
        // maintainAspectRatio:false,
        responsive:true,
    }
}