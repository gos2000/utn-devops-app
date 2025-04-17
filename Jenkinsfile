pipeline {
    agent any

    environment {
        PYTHON_ENV = 'python3'
        PIP = 'pip3'
    }

    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio desde GitHub o cualquier otro origen
                git branch: 'main', url: 'https://github.com/gos2000/utn-devops-app.git'
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    // Instalar Python y Pip si no están instalados
                    sh '''
                        sudo apt update
                        sudo apt install -y python3 python3-pip
                    '''

                    // Instalar las dependencias del proyecto
                    sh "${PIP} install -r requirements.txt"
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    try {
                        // Ejecutar las pruebas unitarias
                        sh "${PYTHON_ENV} -m unittest discover tests"
                        echo "Pruebas unitarias ejecutadas exitosamente."
                    } catch (Exception e) {
                        echo "Error al ejecutar las pruebas unitarias: ${e}"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Build Report') {
            steps {
                script {
                    // Generar un reporte de las pruebas (opcional)
                    sh '''
                        echo "Generando reporte de pruebas..."
                        mkdir -p reports
                        ${PYTHON_ENV} -m unittest discover tests -v > reports/test-results.txt
                    '''
                }
            }
        }
    }

    post {
        always {
            // Limpiar el entorno después de cada ejecución
            cleanWs()
        }
        success {
            echo "El pipeline se completó exitosamente."
        }
        failure {
            echo "El pipeline falló."
        }
    }
}