/**************************
 *  Perceptron Classifier *
 *  Version 1.0           *
 *  by Chin-Sung Lin      *
 *  Date: 01/22/2017      *
 **************************/

#include <stdio.h>
#include <stdlib.h>

#define MAX_PATTERN     1000                                    // set the maximum no. of training patterns

int calculateOutput(float weights[], float x, float y)
{
    float sum = x * weights[2] + y * weights[1] + weights[0];
    return (sum >= 0) ? 1 : -1;
}

int main(int argc, char *argv[])
{
    float x[MAX_PATTERN], y[MAX_PATTERN], weights[3];
    int outputs[MAX_PATTERN], patternCount, i, output;
    int classes, errCount = 0;
    
    FILE *fpatterns;
    FILE *fweights;
    FILE *fclassification;
    
    if ((fweights = fopen("weights.txt", "r")) == NULL) {                     // open weights file.
        printf("Cannot open weights file.\n");
        exit(1);
    }
    
    if ((fpatterns = fopen("testing.txt", "r")) == NULL) {                     // open testing data file.
        printf("Cannot open testing file.\n");
        exit(1);
    }
    fclassification = fopen("classification.txt", "w");
    
    fscanf(fweights, "%f %f %f\n", &weights[2], &weights[1], &weights[0]);    // read weights of trained network.
    
    i = 0;
    while (fscanf(fpatterns, "%f %f %d", &x[i], &y[i], &outputs[i]) != EOF)
        i++;
    patternCount = i;
    fprintf(fclassification, "\nNumber of testing patterns: %d\n", patternCount);
    fprintf(fclassification, "\nDecision boundary (line) equation: %.4f*x + %.4f*y + %.4f = 0\n\n", weights[2], weights[1], weights[0]);
    
    for (i = 0; i < patternCount; i++) {
        output = calculateOutput(weights, x[i], y[i]);
        if (output >= 0)                                                       // convert sign function back to step function
            classes = 1;
        else
            classes = 0;
        
        fprintf(fclassification, "x = %8.4f   y = %8.4f   label = %d   class = %d   ", x[i], y[i], outputs[i], classes);
        if (classes != outputs[i])
        {
            fprintf(fclassification, "*****\n");
            errCount++;
        }
        else
            fprintf(fclassification, "\n");
    }
    
    fprintf(fclassification, "\nError =  %.2f %%\n", (float)errCount/(float)patternCount*100.);      // print out calculated error rate.
    
    return 0;
}
