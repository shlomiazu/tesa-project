@Library('build_an_artifact@v1.0.0') _

pipeline {
    agent any
    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    def scmDetails = prepareEnv(scm: [
                        GIT_COMMIT: '12345abcd',
                        GIT_AUTHOR_NAME: 'shlomi-ibex',
                        GIT_COMMITTER_MESSAGE: 'Initial commit',
                        GIT_BRANCH: 'master'
                    ])
                    echo "SCM Details: ${scmDetails}"
                }
            }
        }
    }
}