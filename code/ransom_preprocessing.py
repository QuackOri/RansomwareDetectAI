import pefile

api_columns = ['API/DLL_1', 'API/DLL_2', 'API/DLL_3', 'API/DLL_4', 'API/DLL_5', 'API/DLL_6', 'API/DLL_7', 'API/DLL_8', 'API/DLL_9', 'API/DLL_10', 'API/DLL_11', 'API/DLL_12', 'API/DLL_13', 'API/DLL_14', 'API/DLL_15', 'API/DLL_16', 'API/DLL_17', 'API/DLL_18', 'API/DLL_19', 'API/DLL_20', 'API/DLL_21', 'API/DLL_22', 'API/DLL_23', 'API/DLL_24', 'API/DLL_25', 'API/DLL_26', 'API/DLL_27', 'API/DLL_28', 'API/DLL_29']
sn_columns = ['SectionName0', 'SectionName1', 'SectionName2', 'SectionName3', 'SectionName4', 'SectionName5', 'SectionName6', 'SectionName7', 'SectionName8', 'SectionName9', 'SectionName10', 'SectionName11', 'SectionName12', 'SectionName13', 'SectionName14', 'SectionName15', 'SectionName16', 'SectionName17', 'SectionName18', 'SectionName19', 'SectionName20', 'SectionName21', 'SectionName22', 'SectionName23', 'SectionName24', 'SectionName25', 'SectionName26', 'SectionName27', 'SectionName28', 'SectionName29', 'SectionName30', 'SectionName31', 'SectionName32', 'SectionName33', 'SectionName34', 'SectionName35', 'SectionName36', 'SectionName37', 'SectionName38', 'SectionName39', 'SectionName40', 'SectionName41', 'SectionName42', 'SectionName43', 'SectionName44', 'SectionName45', 'SectionName46', 'SectionName47', 'SectionName48', 'SectionName49', 'SectionName50', 'SectionName51', 'SectionName52', 'SectionName53', 'SectionName54', 'SectionName55', 'SectionName56', 'SectionName57', 'SectionName58', 'SectionName59', 'SectionName60', 'SectionName61', 'SectionName62', 'SectionName63', 'SectionName64', 'SectionName65', 'SectionName66', 'SectionName67', 'SectionName68', 'SectionName69', 'SectionName70', 'SectionName71', 'SectionName72', 'SectionName73', 'SectionName74', 'SectionName75', 'SectionName76', 'SectionName77', 'SectionName78', 'SectionName79', 'SectionName80', 'SectionName81', 'SectionName82', 'SectionName83', 'SectionName84', 'SectionName85', 'SectionName86', 'SectionName87', 'SectionName88', 'SectionName89', 'SectionName90', 'SectionName91', 'SectionName92', 'SectionName93', 'SectionName94', 'SectionName95', 'SectionName96', 'SectionName97', 'SectionName98', 'SectionName99', 'SectionName100', 'SectionName101', 'SectionName102', 'SectionName103', 'SectionName104', 'SectionName105', 'SectionName106', 'SectionName107', 'SectionName108', 'SectionName109', 'SectionName110', 'SectionName111', 'SectionName112', 'SectionName113', 'SectionName114', 'SectionName115', 'SectionName116', 'SectionName117', 'SectionName118', 'SectionName119', 'SectionName120', 'SectionName121', 'SectionName122', 'SectionName123', 'SectionName124', 'SectionName125', 'SectionName126', 'SectionName127', 'SectionName128', 'SectionName129', 'SectionName130', 'SectionName131', 'SectionName132', 'SectionName133', 'SectionName134', 'SectionName135', 'SectionName136', 'SectionName137', 'SectionName138', 'SectionName139', 'SectionName140', 'SectionName141', 'SectionName142', 'SectionName143', 'SectionName144', 'SectionName145', 'SectionName146', 'SectionName147', 'SectionName148', 'SectionName149', 'SectionName150', 'SectionName151', 'SectionName152', 'SectionName153', 'SectionName154', 'SectionName155', 'SectionName156', 'SectionName157', 'SectionName158', 'SectionName159', 'SectionName160', 'SectionName161', 'SectionName162', 'SectionName163', 'SectionName164', 'SectionName165', 'SectionName166', 'SectionName167', 'SectionName168', 'SectionName169', 'SectionName170', 'SectionName171', 'SectionName172', 'SectionName173', 'SectionName174', 'SectionName175', 'SectionName176', 'SectionName177', 'SectionName178', 'SectionName179', 'SectionName180', 'SectionName181', 'SectionName182', 'SectionName183', 'SectionName184', 'SectionName185', 'SectionName186', 'SectionName187', 'SectionName188', 'SectionName189', 'SectionName190', 'SectionName191', 'SectionName192', 'SectionName193', 'SectionName194', 'SectionName195', 'SectionName196', 'SectionName197', 'SectionName198', 'SectionName199', 'SectionName200', 'SectionName201', 'SectionName202', 'SectionName203', 'SectionName204', 'SectionName205', 'SectionName206', 'SectionName207', 'SectionName208', 'SectionName209', 'SectionName210', 'SectionName211', 'SectionName212', 'SectionName213', 'SectionName214', 'SectionName215', 'SectionName216', 'SectionName217', 'SectionName218', 'SectionName219', 'SectionName220', 'SectionName221', 'SectionName222', 'SectionName223', 'SectionName224', 'SectionName225', 'SectionName226', 'SectionName227', 'SectionName228', 'SectionName229', 'SectionName230']

section_names = ['', 'rSEkROYX', 'jUtrpYsA', 'KwTbCaxM', '.rvtn', '.ajelhf', '.tls \x10', 'CODE', '.embm', '.retplne', 'waecTbTU', '.toour', '.reloc', '.itext', 'DvWhCIvf', '.edata', 'aMzuGtCo', '.idata', 'UPX2', '.nvFatBi', '.aspack', '.pr1', 'rbqkwszv', '30186', '.itext \x10', '.enigma1', '.eryi', '.pr0', 'PARTUrmq', '.f', '.fasm', 'QwJTpjYY', 'XkeFCeIk', '.l1', 'pVQaXXRZ', 'zixCLRPo', '.UPX0', 'seg2', 'hjsUDrdI', '.atu', 'zCOudfzz', '.wdata', '.didata', 'brlYMzrk', 'iqsNyMnI', 'UPX0', 'text', '191128', '.gl', '\x10Z \x1b@\x12\x19\x01', 'uByjmpOk', '.enigma2', 'rQgajwSl', '111149', '.pdata', 'cofrmms', '.hnmtr', 'OnAQWSnT', '.hoAiXT', '.zqi', '19199', 'dkdxbvi', '.xObf', 'uAsLxMSc', '.fen', '.text U', 'XBqaJfNA', 'seg1', '241105', 'IRevzthI', '.ksj', '23233', '.text no', 'SmAxvlLA', 'DZPWkQjd', 'stub', 'lzPiGjjl', 'ajHuyfDz', 'GlFCfAHi', 'gtmVsfxT', 'fTBAqfyw', 'data', '/4', '.xjs', 'PAGED', '.rsrc \x10', '11988', '.avtpq', 'gTqpRBSE', '7162', '16678', '.text', '.msvcjmc', 'bdbhKMcA', '.xdata', '_TEXT_CN', '5227', 'BSS', 'ZXpdpZCG', '.ygz', 'TEXT', '.aajaic', 'gZnBDeJg', '.rsrc', 'NET', '.fmbav', 'XPoQQDfw', 'DcGfkoSu', '.yxutw', 'UPX1', '15399', '.nv_fatb', 'oMRJGIsK', '.data', 'cWWlXjsE', 'petite', '.textbss', '24081', '2814', 'mufJjTLu', '&1em&1em', '.rsrc s', 'qNVHhmNz', '.uebh', '.d', '.petite', 'VntOSupj', 'g53zp4v8', 'tcOPuqRW', '.shr', '.imrsiv', '.', '.vmp1', '.l2', '.ap0x', '.gnu_deb', 'JSCnruWr', '.srdata', '.gfcd', '215178', '.data U', '.turt', '.vaet', '.reloc \x10', 'aCJMwlGU', '.00cfg', 'iiHYouMw', '.CRT', 'tvCfQlYx', '.flh', '.ieoo', '.xbyi', '.idata \x10', '.rodata', '.vmp0', 'yvsVDYin', '.adata', 'PGGiDbVj', 'sYndfJsm', 'rGTbDTJs', '.now', 'kwVuDSUh', 'gYyYNFDp', '.NewSec', '.wtf', 'cKHqNuzk', '.zxx', 'PnImEyie', '.ndata', '.tls', 'DATA', '.zbpf', 'gMssCbqf', 'BovETaNi', 'OLkGuECx', 'VHGShZYj', 'rGfFyqXK', '188120', 'CODE \x10', 'kMfgwsmE', '.rdata', '.code', 'INIT', '1', 'DMYJwSiy', '.pebizo', '.sdata', '.idata o', 'ZXwPlvTQ', 'YohejkEe', 'GFIDS', 'CPADinfo', '.bss', '.text \x10', '.imports', 'nPcvodWH', '.didat', '.kx', 'YkVgPvyv', 'ttSMtSxz', 'PAGE', '.p', '.cdata', 'ZTBOXsdz', 'bss \x10', 'cnwnFlwT', '.data \x10', 'LQVNEPly', '.zfe', '.fldo', 'wjfwhyr', '.MPRESS2', '.icode', '.a57y2', 'JCYholgx', '.sg', '.vbp', '.code \x12', 'kUHiTJjx', '16386', '.gfids', '.guids', '23815', '.MPRESS1', 'fPisKdRT', '_RDATA', '.lfd', '.modplug', '.ick', '.y', '16165']
desired_features = {
1: [
    "CreateFileA",  # 파일 생성
    "SetFileAttributesA",  # 파일 속성 설정
    "GetFileAttributesW",  # 파일 속성 가져오기 (Wide 문자열)
    "GetFileAttributesExW",  # 파일 속성 및 정보 가져오기 (Wide 문자열)
    "GetFileInformationByHandle",  # 파일 정보 가져오기
    "ReadDirectoryChangesW",  # 디렉터리 변경 사항 모니터링
    "FindClose",  # 파일 검색 핸들 닫기
    "FindFirstFileExA",  # 첫 번째 파일 검색 (Extended API, ANSI 문자열)
    "FindNextFileA",  # 다음 파일 검색 (ANSI 문자열)
    "FindNextFileW"  # 다음 파일 검색 (Wide 문자열)
],

# 네트워크 통신
2: [
    "IcmpCreateFile",  # ICMP 통신 파일 생성
    "IcmpSendEcho"  # ICMP 에코 요청 보내기
],

# 네트워크 정보 및 서버/공유 관리
3: [
    "GetAdaptersInfo",  # 네트워크 어댑터 정보 가져오기
    "NetServerEnum",  # 서버 목록 열거
    "NetShareEnum",  # 공유 목록 열거
    "NetApiBufferFree"  # API 버퍼 해제
],

# 네트워크 소켓 관리
4: [
    "WSACleanup",  # Windows 소켓 라이브러리 정리
    "WSAStartup",  # Windows 소켓 라이브러리 초기화
    "socket",  # 소켓 생성
    "closesocket",  # 소켓 닫기
    "connect",  # 소켓 연결
    "gethostbyname",  # 호스트 이름에 대한 정보 가져오기
    "send",  # 데이터 보내기
    "inet_ntoa",  # IP 주소를 문자열로 변환
    "htons"  # 호스트 바이트 순서를 네트워크 바이트 순서로 변환
],

# 암호화 키 및 데이터 처리
5: [
    "CryptImportPublicKeyInfo",  # 공개 키 정보 가져오기
    "CryptStringToBinaryA",  # 문자열을 이진 데이터로 변환 (ANSI 문자열)
    "CryptDecodeObjectEx",  # 암호화 객체 디코딩
    "CryptEncrypt",  # 데이터 암호화
    "CryptImportKey",  # 키 가져오기
    "CryptSetKeyParam",  # 키 매개 변수 설정
    "CryptDestroyKey",  # 키 제거
    "CryptReleaseContext",  # 암호화 컨텍스트 해제
    "CryptAcquireContextA"  # 암호화 컨텍스트 얻기 (ANSI 문자열)
],

# 시스템 정보 관리
6: [
    "GetVersion",  # Windows 버전 정보 가져오기
    "GetLastError",  # 마지막 오류 코드 가져오기
    "Sleep",  # 실행 중인 스레드를 일정 시간 동안 중지
    "GetTickCount",  # 시스템 시작 이후 경과 시간(밀리초) 가져오기
    "GetModuleFileNameA",  # 모듈 파일 이름 가져오기 (ANSI 문자열)
    "GetSystemDirectoryA"  # 시스템 디렉터리 경로 가져오기 (ANSI 문자열)
],

# 현재 프로세스 정보
7: [
    "GetCurrentProcess",  # 현재 실행 중인 프로세스 핸들 가져오기
    "GetCurrentProcessId",  # 현재 실행 중인 프로세스 ID 가져오기
    "GetProcessHeap"  # 프로세스 힙 핸들 가져오기
],

# 프로세스 및 스레드 생성
8: [
    "CreateThread",  # 스레드 생성
    "CreateEventW"  # 이벤트 생성 (Wide 문자열)
],

# 스레드 관리
9: [
    "GetCurrentThreadId",  # 현재 스레드 ID 가져오기
    "TerminateThread",  # 스레드 종료
    "ResumeThread",  # 스레드 재개
    "GetCurrentThread",  # 현재 스레드 핸들 가져오기
    "GetThreadPriority",  # 스레드 우선순위 가져오기
    "SetThreadPriority"  # 스레드 우선순위 설정
],

# 스레드 및 프로세스 종료
10: [
    "TerminateProcess",  # 프로세스 종료
    "ExitThread"  # 스레드 종료
],

# 동기화 및 이벤트
11: [
    "WaitForSingleObject",  # 단일 객체 대기
    "WaitForSingleObjectEx",  # 단일 객체 대기 (확장)
    "SwitchToThread",  # 다른 스레드로 전환
    "RegisterWaitForSingleObject",  # 개체 대기 등록
    "UnregisterWait",  # 개체 대기 등록 취소
    "GetThreadTimes"  # 스레드 시간 정보 가져오기
],

# 메모리 할당 및 해제
12: [
    "GlobalAlloc",  # 전역 메모리 할당
    "GlobalFree",  # 전역 메모리 해제
    "HeapSize",  # 힙 크기 가져오기
    "HeapFree",  # 힙 해제
    "HeapReAlloc",  # 힙 재할당
    "HeapAlloc"  # 힙 할당
],

# 메모리 보호
13: [
    "EncodePointer",  # 포인터 인코딩
    "DecodePointer"  # 포인터 디코딩
],

# 스레드 안전성
14: [
    "InterlockedPopEntrySList",  # 스택 리스트에서 항목 빼기
    "InterlockedPushEntrySList",  # 스택 리스트에 항목 추가
    "InterlockedFlushSList",  # 스택 리스트 플러시
    "QueryDepthSList",  # 스택 리스트 깊이 조회
    "UnregisterWaitEx"  # 개체 대기 등록 취소 (확장)
],

# 윈도우즈 API 및 라이브러리 관리
15: [
    "LoadLibraryA",  # 라이브러리 로드 (ANSI 문자열)
    "FindResourceA",  # 리소스 찾기 (ANSI 문자열)
    "LoadResource",  # 리소스 로드
    "SizeofResource",  # 리소스 크기 가져오기
    "GetProcAddress",  # 함수 주소 가져오기
    "GetStartupInfoW",  # 시동 정보 가져오기 (Wide 문자열)
    "GetCommandLineA",  # 명령줄 가져오기 (ANSI 문자열)
    "GetCommandLineW",  # 명령줄 가져오기 (Wide 문자열)
    "GetEnvironmentStringsW",  # 환경 문자열 가져오기 (Wide 문자열)
    "GetConsoleCP",  # 콘솔 코드 페이지 가져오기
    "FreeEnvironmentStringsW",  # 환경 문자열 해제 (Wide 문자열)
    "SetEnvironmentVariableA",  # 환경 변수 설정 (ANSI 문자열)
    "FreeLibrary",  # 라이브러리 해제
    "FreeLibraryAndExitThread",  # 라이브러리 해제 및 스레드 종료
    "LoadLibraryExW",  # 라이브러리 로드 (Wide 문자열)
    "LoadLibraryW"  # 라이브러리 로드 (Wide 문자열)
],

# 윈도우즈 API 함수
16: [
    "EnumSystemLocalesW",  # 시스템 로캘 열거 (Wide 문자열)
    "GetUserDefaultLCID",  # 사용자 기본 로캘 식별자 가져오기
    "GetConsoleMode",  # 콘솔 모드 가져오기
    "ReadFile",  # 파일 읽기
    "ReadConsoleW",  # 콘솔에서 읽기 (Wide 문자열)
    "SetFilePointerEx"  # 파일 포인터 설정 (확장)
],

# 문자 인코딩 및 로캘 정보
17: [
    "GetACP",  # 활성 코드 페이지 가져오기
    "FormatMessageW"  # 형식화된 메시지 가져오기 (Wide 문자열)
],

# 핸들 관리
18: [
    "DuplicateHandle",  # 핸들 복제
    "CloseHandle"  # 핸들 닫기
],

# 크리티컬 섹션 관리
19: [
    "EnterCriticalSection",  # 크리티컬 섹션 진입
    "LeaveCriticalSection",  # 크리티컬 섹션 떠나기
    "TryEnterCriticalSection",  # 크리티컬 섹션 시도 진입
    "DeleteCriticalSection"  # 크리티컬 섹션 삭제
],

# 로캘 정보 관리
20: [
    "IsValidLocale"  # 유효한 로캘 확인
],

# 오류 처리 관리
21: [
    "SetLastError"  # 마지막 오류 코드 설정
],

# 콘솔 관리
22: [
    "SetStdHandle"  # 표준 핸들 설정
],

# 콘솔 입력 및 출력
23: [
    "WriteConsoleW"  # 콘솔에 쓰기 (Wide 문자열)
],
24: [
    "GetOEMCP",  # OEM 코드 페이지 가져오기
    "SetUnhandledExceptionFilter",  # 처리되지 않은 예외 필터 설정
    "CreateMutexA",  # 뮤텍스 생성 (ANSI 문자열)
    "ReleaseMutex",  # 뮤텍스 해제
    "CloseHandle"  # 핸들 닫기
],

# 타이머 및 이벤트 관리
25: [
    "CreateTimerQueue",  # 타이머 큐 생성
    "SignalObjectAndWait",  # 객체 신호 및 대기
    "CreateTimerQueueTimer",  # 타이머 큐 타이머 생성
    "ChangeTimerQueueTimer",  # 타이머 큐 타이머 변경
    "DeleteTimerQueueTimer",  # 타이머 큐 타이머 삭제
    "QueryPerformanceCounter",  # 성능 카운터 조회
    "CreateEventW"  # 이벤트 생성 (Wide 문자열)
],

# 레지스트리 관리
26: [
    "RegSetValueExA",  # 레지스트리 값 설정 (ANSI 문자열)
    "RegOpenKeyA",  # 레지스트리 키 열기 (ANSI 문자열)
    "RegDeleteValueA",  # 레지스트리 값 삭제 (ANSI 문자열)
    "RegCloseKey"  # 레지스트리 키 닫기
],

# 파일 시스템 및 볼륨 관리
27: [
    "SHGetSpecialFolderPathA",  # 특수 폴더 경로 가져오기 (ANSI 문자열)
    "SHEmptyRecycleBinA",  # 휴지통 비우기 (ANSI 문자열)
    "ShellExecuteA"  # 외부 프로그램 실행 (ANSI 문자열)
],

# 사용자 및 시스템 정보 관리
28: [
    "GetUserNameA",  # 사용자 이름 가져오기 (ANSI 문자열)
    "GetComputerNameA"  # 컴퓨터 이름 가져오기 (ANSI 문자열)
],

# 가상 디스크 관리
29: [
    "RmEndSession",  # 세션 종료
    "RmGetList",  # 세션 목록 가져오기
    "RmStartSession",  # 세션 시작
    "AttachVirtualDisk",  # 가상 디스크 연결
    "GetVirtualDiskPhysicalPath",  # 가상 디스크의 실제 경로 가져오기
    "OpenVirtualDisk"  # 가상 디스크 열기
]
}

def pre_sectionname(path):
    pe = pefile.PE(path)
    row = [0] * len(section_names)
    for section in pe.sections:
        section_name = section.Name.decode('utf8').rstrip('\x00')
        for i, s in enumerate(section_names):
            if s == section_name:
                row[i] += 1
    
    return row

def extract_api_functions(file_path):
    # API 추출 로직 ()
    try:
        pe = pefile.PE(file_path)
        api_functions = []

        # 파일의 Import 디스크립터에서 API 함수 목록 추출
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            for imp in entry.imports:
                api_functions.append(imp.name.decode('utf-8'))

        return api_functions

    except Exception as e:
        return []

def pre_api(path):
    apis = extract_api_functions(path)
    label_values = [0] * 29  # 그룹 레이블별 카운터를 저장하기 위한 리스트 초기화
    for index, group_features in desired_features.items():
        label_value = 0
        for feature in group_features:
            if feature in apis:
                label_value += 1  # API 함수가 발견될 때마다 카운터 증가
        label_values[index-1] = label_value  # 카운터를 저장
    return label_values

if __name__=="__main__":
    target_path = 'C:\\Users\\manseo\\Desktop\\finalAI\\testdata\\131.exe'
    #print(pre_sectionname(target_path))
    print(pre_api(target_path))
