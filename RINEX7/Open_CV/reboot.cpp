#include <iostream>
#include <Windows.h>

void Reboot() {
    std::cout << "Rebooting...";

    HANDLE hToken;
    TOKEN_PRIVILEGES tkp;

    // Get a token for this process.
    if (!OpenProcessToken(GetCurrentProcess(), TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &hToken)) {
        std::cout << "Failed to get process token.\n";
        return;
    }

    // Get the LUID for the shutdown privilege.
    LookupPrivilegeValue(NULL, SE_SHUTDOWN_NAME, &tkp.Privileges[0].Luid);

    tkp.PrivilegeCount = 1;
    tkp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;

    // Get the shutdown privilege for this process.
    if (!AdjustTokenPrivileges(hToken, FALSE, &tkp, 0, (PTOKEN_PRIVILEGES)NULL, 0)) {
        std::cout << "Failed to get shutdown privilege.\n";
        return;
    }

    // Reboot the computer.
    if (!ExitWindowsEx(EWX_REBOOT, 0)) {
        std::cout << "Failed to reboot computer.\n";
        return;
    }

    std::cout << "Computer rebooted successfully.\n";
}

int main() {
    Reboot();
    return 0;
}