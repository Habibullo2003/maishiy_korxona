document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('faoliyatChart');

    if (ctx) {
        const labels = JSON.parse(ctx.dataset.labels);
        const values = JSON.parse(ctx.dataset.values);

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Korxonalar soni',
                    data: values,
                    backgroundColor: 'rgba(46, 125, 50, 0.7)',
                    borderColor: 'rgba(46, 125, 50, 1)',
                    borderWidth: 2,
                    borderRadius: 5
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            font: {
                                size: 14
                            }
                        }
                    },
                    title: {
                        display: true,
                        text: 'Korxonalar faoliyat turlari bo‘yicha',
                        font: {
                            size: 18
                        }
                    },
                    tooltip: {
                        enabled: true,
                        callbacks: {
                            label: function (context) {
                                return `${context.dataset.label}: ${context.raw} ta`;
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 1
                        }
                    }
                }
            }
        });
    }
});
