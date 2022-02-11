#include <stdio.h>

#include <math.h>

#define COL 300
//input/binary/line images column number

#define ROW 200
//input/binary/line images row number

#define STR_LENGTH 30
//file name string length

int main(int argc, const char * argv[]){

unsigned int i, j;
//row and column index

unsigned int img_inp[ROW][COL];
//input image

char input_filename[STR_LENGTH];
//input file name string

FILE *in_file;
//input image file

FILE *out_file;
//output image file

char ppm_file_type[STR_LENGTH];
//file type string

unsigned int ppm_column; //number of rows in ppm file

unsigned int ppm_row; //number of columns in ppm file

unsigned int ppm_color;
//number of colors in ppm file

unsigned int dmy = 0; //garbage can

printf("Input Image File: ");
//Ask user input file name

scanf ("%s", input_filename);
// Read filename from command line

/** File Open **/

in_file = fopen(input_filename,"r");
//open input image file

out_file = fopen ("art.ppm","w");
//open output image file

/** Read Input Image Headers **/

fscanf (in_file, "%s", ppm_file_type);
//read ppm file type

fscanf (in_file, "%d", &ppm_column);
//read ppm column number

fscanf (in_file, "%d", &ppm_row);
//read ppm row number

fscanf (in_file, "%d", &ppm_color);
//read ppm color number