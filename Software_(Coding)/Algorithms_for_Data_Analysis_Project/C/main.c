#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

// Hashtable Constants
#define SIZE 20

// File read Constants
#define FILESIZE 10
#define STRINGLENGTH 15

/* Code For Hashtable ----------------------------------------------*/
struct DataItem {
   int data;   
   int key;
};

struct DataItem* hashArray[SIZE]; 
struct DataItem* hashtable;
struct DataItem* item;

int hashCode(int key) {
   return key % SIZE;
}

struct DataItem *search(int key) {
   //get the hash 
   int hashIndex = hashCode(key);  
	
   //move in array until an empty 
   while(hashArray[hashIndex] != NULL) {
	
      if(hashArray[hashIndex]->key == key)
         return hashArray[hashIndex]; 
			
      //go to next cell
      ++hashIndex;
		
      //wrap around the table
      hashIndex %= SIZE;
   }        
	
   return NULL;        
}

void insert(int key, int data) {

   struct DataItem *item = (struct DataItem*) malloc(sizeof(struct DataItem));
   item->data = data;  
   item->key = key;

   //get the hash 
   int hashIndex = hashCode(key);

   //move in array until an empty or deleted cell
   while(hashArray[hashIndex] != NULL && hashArray[hashIndex]->key != -1) {
      //go to next cell
      ++hashIndex;
		
      //wrap around the table
      hashIndex %= SIZE;
   }
	
   hashArray[hashIndex] = item;
}

struct DataItem* delete(struct DataItem* item) {
   int key = item->key;

   //get the hash 
   int hashIndex = hashCode(key);

   //move in array until an empty
   while(hashArray[hashIndex] != NULL) {
	
      if(hashArray[hashIndex]->key == key) {
         struct DataItem* temp = hashArray[hashIndex]; 
			
         //assign a dummy item at deleted position
         hashArray[hashIndex] = hashtable; 
         return temp;
      }
		
      //go to next cell
      ++hashIndex;
		
      //wrap around the table
      hashIndex %= SIZE;
   }      
	
   return NULL;        
}

void display() {
   int i = 0;
	
   for(i = 0; i<SIZE; i++) {
	
      if(hashArray[i] != NULL)
         printf(" (%d,%d)",hashArray[i]->key,hashArray[i]->data);
      else
         printf(" ~~ ");
   }
	
   printf("\n");
}

/* -----------------------------------------------------------------*/


/* Code For File Reading -------------------------------------------*/

// Read and Write Strings and Integers from and to Files


// int fileread() {

// FILE* fileInput = NULL;
// FILE* fileOutput = NULL;

// char str[FILESIZE][STRINGLENGTH];
// int number[FILESIZE];

// fileInput = fopen("input.txt", "r");

// fileOutput = fopen("output.txt", "w");

// for (int i = 0; i < FILESIZE; i++)
//    fscanf (fileInput, "%s %d", str[i], &number[i]);

// for (int i = 0; i < FILESIZE; i++)
//    fprintf(fileOutput, "string[%d] = %13s, number[%d] = %3d\n\n", i, str[i], i, number[i]*2);
// for (int i = 0; i < FILESIZE; i++)
//    fprintf(fileOutput, "%s ", str[i]);

// fprintf(fileOutput, "\n\n");
// fclose(fileInput);
// fclose(fileOutput);


/* -----------------------------------------------------------------*/



int main() {
   hashtable = (struct DataItem*) malloc(sizeof(struct DataItem));
   hashtable->data = -1;  
   hashtable->key = -1;

   int int_values[2] = {20, 20};

   insert(1, int_values);
   insert(2, 70);
   insert(42, 80);
   insert(4, 25);
   insert(12, 44);
   insert(14, 32);
   insert(17, 11);
   insert(13, 78);
   insert(37, 97);

   display();
   item = search(37);

   if(item != NULL) {
      printf("Element found: %d\n", item->data);
   } else {
      printf("Element not found\n");
   }

   delete(item);
   item = search(37);

   if(item != NULL) {
      printf("Element found: %d\n", item->data);
   } else {
      printf("Element not found\n");
   }
}