struct ListNode {
public:
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {};
    ListNode(int v) : val(v), next(nullptr) {};
    ListNode(int v, ListNode* next) : val(v), next(next) {};
};


class MyLinkedList {
public:
    /** Initialize your data structure here. */
    MyLinkedList() {

    }

    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        ListNode* cur = head;
        for (int i = 0; i < index; ++i) {
            if (!cur) return -1;
            cur = cur->next;
        }
        if (cur) return cur->val;
        else return -1;
    }

    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        ListNode* newHead = new ListNode(val, head);
        head = newHead;
    }

    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        ListNode* cur = head;
        ListNode* newTail = new ListNode(val);
        if (!cur) {
            head = newTail;
            return;
        }
        while (cur->next) {
            cur = cur->next;
        }
        cur->next = newTail;
    }

    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        ListNode* cur = head;
        if (index == 0) {
            ListNode* newNode = new ListNode(val, head);
            head = newNode;
            return;
        }
        for (int i = 0; i < index-1; ++i) {
            if (!cur) return;
            cur = cur->next;
        }
        if (!cur) return;
        ListNode* newNode = new ListNode(val, cur->next);
        cur->next = newNode;
    }

    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        ListNode* cur = head;
        if (index == 0) {
            head = head->next;
            delete cur;
            return;
        }
        for (int i = 0; i < index - 1; ++i) {
            if (!cur) return;
            cur = cur->next;
        }
        if (!cur || !cur->next) return;
        ListNode* temp = cur->next;
        cur->next = temp->next;
        delete temp;
    }

private:
    ListNode* head = nullptr;
};


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */