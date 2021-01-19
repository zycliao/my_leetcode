#include<vector>
#include<iostream>


struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* new_head = head;
        ListNode* prev = nullptr, *node = head;
        while (node) {
            if (node->val == val) {
                if (prev) {
                    prev->next = node->next;
                    delete node;
                    node = prev->next;
                }
                else {
                    prev = node;
                    node = node->next;
                    new_head = node;
                    delete prev;
                    prev = nullptr;
                }
            }
            else {
                prev = node;
                node = node->next;
            }
        }
        return new_head;
    }
};

// dummy head method
class Solution2 {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummyHead = new ListNode(0, head);
        ListNode* prev = dummyHead, * node = head;
        while (node) {
            if (node->val == val) {
                prev->next = node->next;
                delete node;
                node = prev->next;
            }
            else {
                prev = node;
                node = node->next;
            }
        }
        return dummyHead->next;
    }
};



ListNode* createList(std::vector<int> x)
{
    ListNode *head = nullptr, *prev = nullptr;
    for (int i = 0; i < x.size(); ++i) {
        ListNode* node = new ListNode(x[i]);
        if (i == 0)
            head = node;
        else
            prev->next = node;
        prev = node;
    }
    return head;
}


void printList(ListNode* node) {
    while (node) {
        std::cout << node->val << " ";
        node = node->next;
    }
    std::cout << std::endl;
}


int main()
{
    std::vector<int> x {1, 1};
    int val = 1;
    // create linked list
    ListNode* head = createList(x);
    printList(head);
    auto sol = Solution();
    ListNode* res = sol.removeElements(head, val);
    printList(res);
}