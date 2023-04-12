#include<simplecpp>

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Function to add a new node to the linked list
void addNode(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = *head_ref;
    *head_ref = new_node;
}

// Function to delete a particular node referenced by the location
void deleteNode(struct Node** head_ref, int position) {
    if (*head_ref == NULL) return;
    struct Node* temp = *head_ref;
    if (position == 0) {
        *head_ref = temp->next;
        free(temp);
        return;
    }
    for (int i = 0; temp != NULL && i < position - 1; i++) temp = temp->next;
    if (temp == NULL || temp->next == NULL) return;
    struct Node* next = temp->next->next;
    free(temp->next);
    temp->next = next;
}

// Function to delete all nodes from the list which contain a particular data
void deleteNodesWithData(struct Node** head_ref, int data) {
    struct Node* current = *head_ref;
    struct Node* prev = NULL;
    while (current != NULL) {
        if (current->data == data) {
            if (prev == NULL) {
                *head_ref = current->next;
            } else {
                prev->next = current->next;
            }
            free(current);
            current = (prev == NULL) ? *head_ref : prev->next;
        } else {
            prev = current;
            current = current->next;
        }
    }
}

// Function to delete the complete linked list
void deleteList(struct Node** head_ref) {
    struct Node* current = *head_ref;
    struct Node* next;
    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
    *head_ref = NULL;
}

// Function to display the linked list
void displayList(struct Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

// Function to display the inverted linked list
void displayInvertedList(struct Node* node) {
    if (node == NULL) return;
    displayInvertedList(node->next);
    printf("%d ", node->data);
}

// Function to display the total memory space occupied by the linked list
int displayMemoryUsage(struct Node* node) {
    int total = 0;
    while (node != NULL) {
        total += sizeof(struct Node);
        node = node->next;
    }
    return total;
}

