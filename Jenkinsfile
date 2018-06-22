#!groovy

environment { 
    IMAGE = "bearn/testapp
}

node {

    currentBuild.result = "SUCCESS"

    try {

       stage('Checkout'){

          checkout scm
       }

       stage('Test'){

           sh 'printenv'

       }

       stage('Build Docker'){

           sh 'docker build --pull --cache-from ${env.IMAGE} -t ${env.IMAGE} .'
       }

       stage('Deploy'){

         echo 'Push to Repo'

       }

       stage('Cleanup'){

         echo 'prune and cleanup'
 /*        mail body: 'project build successful',
                     from: 'xxxx@yyyyy.com',
                     replyTo: 'xxxx@yyyy.com',
                     subject: 'project build successful',
                     to: 'yyyyy@yyyy.com' */
       }



    }
    catch (err) {

        currentBuild.result = "FAILURE"

/*            mail body: "project build error is here: ${env.BUILD_URL}" ,
            from: 'xxxx@yyyy.com',
            replyTo: 'yyyy@yyyy.com',
            subject: 'project build failed',
            to: 'zzzz@yyyyy.com' */

        throw err
    }

}
