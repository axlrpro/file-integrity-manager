# file-integrity-manager
A File Integrity Monitor (FIM) is used by cybersecurity professionals to detect unauthorised changes to files in a system. This can be used to protect a machine from malware injection and other exploits related with malicious files.

## Process
This program works as follows:

```mermaid
flowchart TD
    A[Start] -->|input: path| B[Check if path exists in record];
    B--> |path exists| C[Ask user what to do:\nA - Create image\nB - Compare image];
    B--> |path doesn't exist| D[Add path to record];
    D-->C;
    C--> |A| E[Calculate hash for each file\nStore hash in image.txt];
    C--> |B| F[Load file:hash from image.txt\nFor each file -\n1. Calculate hash\n2.Compare against existing hash];
    F-->F;
    F--> G[Hash doesn't match: File changed\nHash doesn't exist: New file\nFile doesn't exist: File deleted];
```

## Usage
    python fm.py <path>
Path should be of a folder which contains only files and not any other folder inside of it

### 1. Adding a new folder to records
![image](https://github.com/axlrpro/file-integrity-manager/assets/38007584/4dd5c449-513b-4b6c-b4b2-4eb0c0042498)

### 2. Updating image
![image](https://github.com/axlrpro/file-integrity-manager/assets/38007584/ef0fb2a8-ad67-4252-a957-aa72fdc1b5c9)

### 3. Compare with existing image
![image](https://github.com/axlrpro/file-integrity-manager/assets/38007584/0cbc7ad2-8bec-488b-bd3e-e6f13d412e10)

### 4. A file content is changed
![image](https://github.com/axlrpro/file-integrity-manager/assets/38007584/9145faa5-8734-4d49-865a-0860cf753425)

### 5. A file is deleted
![image](https://github.com/axlrpro/file-integrity-manager/assets/38007584/f5b2819a-2455-446d-9785-f5f6c27b7094)

### 6. A new file is created
![image](https://github.com/axlrpro/file-integrity-manager/assets/38007584/a0564b72-d52f-44ef-9fe2-b52395bc0fd0)

