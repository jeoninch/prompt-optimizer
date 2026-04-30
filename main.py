#!/usr/bin/env python3
import click
import sys
from colorama import Fore, Style, init
from optimizer import PromptOptimizer

# Initialize colorama for cross-platform colored output
init(autoreset=True)


class PromptOptimizerCLI:
    """CLI interface for prompt optimizer"""

    def __init__(self):
        self.optimizer = PromptOptimizer()

    def print_header(self, title: str):
        """Print a formatted header"""
        click.echo(
            f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}"
        )
        click.echo(f"{Fore.CYAN}{title}{Style.RESET_ALL}")
        click.echo(
            f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n"
        )

    def print_section(self, title: str, content: str, color=Fore.WHITE):
        """Print a formatted section"""
        click.echo(f"{Fore.YELLOW}📊 {title}{Style.RESET_ALL}")
        click.echo(f"{color}{content}{Style.RESET_ALL}\n")

    def print_stats(self, stats: dict):
        """Print comparison statistics"""
        click.echo(f"{Fore.GREEN}✨ Optimized Prompt{Style.RESET_ALL}")
        click.echo(f"{Fore.CYAN}Tokens: {stats['optimized_tokens']}\n{Style.RESET_ALL}")

    def print_savings(self, stats: dict):
        """Print token savings"""
        saved = stats['saved_tokens']
        percent = stats['savings_percent']
        click.echo(
            f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}"
        )
        click.echo(
            f"{Fore.GREEN}💰 Savings: {saved} tokens "
            f"({percent:.1f}% reduction){Style.RESET_ALL}"
        )
        click.echo(
            f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}\n"
        )

    def print_changes(self, changes: list):
        """Print optimization changes"""
        if changes:
            click.echo(f"{Fore.MAGENTA}💡 Optimization Changes{Style.RESET_ALL}")
            for change in changes[:10]:  # Show max 10 changes
                click.echo(f"  {Fore.MAGENTA}•{Style.RESET_ALL} {change}")
            if len(changes) > 10:
                click.echo(f"  {Fore.MAGENTA}... and {len(changes)-10} more{Style.RESET_ALL}")
            click.echo()

    def display_comparison(self, original: str, optimized: str, stats: dict, changes: list):
        """Display side-by-side comparison"""
        self.print_header("📊 Original Prompt")
        click.echo(f'{Fore.WHITE}"{original}"{Style.RESET_ALL}\n')
        click.echo(
            f"{Fore.CYAN}Tokens: {stats['original_tokens']}\n{Style.RESET_ALL}"
        )

        self.print_header("✨ Optimized Prompt")
        click.echo(f'{Fore.GREEN}"{optimized}"{Style.RESET_ALL}\n')
        click.echo(
            f"{Fore.GREEN}Tokens: {stats['optimized_tokens']}\n{Style.RESET_ALL}"
        )

        self.print_header("💡 Optimization Changes")
        self.print_changes(changes)

        self.print_savings(stats)

    def show_menu(self):
        """Show main menu and get user choice"""
        click.echo(f"{Fore.YELLOW}Selection:{Style.RESET_ALL}")
        click.echo(f"  {Fore.CYAN}[1]{Style.RESET_ALL} Optimized Prompt Copy")
        click.echo(f"  {Fore.CYAN}[2]{Style.RESET_ALL} Original Prompt Copy")
        click.echo(f"  {Fore.CYAN}[3]{Style.RESET_ALL} Re-optimize")
        click.echo(f"  {Fore.CYAN}[q]{Style.RESET_ALL} Cancel\n")

        choice = click.prompt("Input", type=str).lower().strip()
        return choice

    def process_prompt(self, prompt: str, show_menu: bool = True):
        """Process and optimize a prompt"""
        if not prompt or not prompt.strip():
            click.echo(f"{Fore.RED}❌ Empty prompt provided.{Style.RESET_ALL}")
            return

        # Optimize
        optimized, changes = self.optimizer.optimize(prompt)

        # Compare
        stats = self.optimizer.compare(prompt, optimized)

        # Check if optimization was effective
        if optimized.strip() == prompt.strip():
            click.echo(f"{Fore.YELLOW}ℹ️  The prompt is already optimized!{Style.RESET_ALL}\n")
            return

        # Display
        self.display_comparison(prompt, optimized, stats, changes)

        if not show_menu:
            return

        # Menu
        while True:
            choice = self.show_menu()

            if choice == '1':
                click.echo(
                    f"{Fore.GREEN}✅ Optimized Prompt:{Style.RESET_ALL}\n"
                    f'{optimized}\n'
                )
                break
            elif choice == '2':
                click.echo(
                    f"{Fore.CYAN}ℹ️  Original Prompt:{Style.RESET_ALL}\n"
                    f'{prompt}\n'
                )
                break
            elif choice == '3':
                # Re-optimize the optimized prompt
                re_optimized, re_changes = self.optimizer.optimize(optimized)
                stats = self.optimizer.compare(optimized, re_optimized)
                self.display_comparison(optimized, re_optimized, stats, re_changes)
            elif choice == 'q':
                click.echo(f"{Fore.YELLOW}❌ Canceled.{Style.RESET_ALL}")
                break
            else:
                click.echo(f"{Fore.RED}❌ Invalid choice.{Style.RESET_ALL}")

    def interactive_mode(self):
        """Run interactive mode"""
        click.clear()
        click.echo(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        click.echo(f"{Fore.CYAN}🚀 Prompt Optimizer - interactive mode{Style.RESET_ALL}")
        click.echo(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")

        while True:
            try:
                prompt = click.prompt(
                    f"{Fore.YELLOW}Input prompt (type 'exit' to quit){Style.RESET_ALL}"
                )

                if prompt.lower() == 'exit':
                    click.echo(f"{Fore.CYAN}Goodbye! 👋{Style.RESET_ALL}")
                    break

                self.process_prompt(prompt, show_menu=True)

            except KeyboardInterrupt:
                click.echo(f"\n{Fore.YELLOW}Canceled.{Style.RESET_ALL}")
                break
            except Exception as e:
                click.echo(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")


@click.command()
@click.option(
    '-p', '--prompt',
    type=str,
    help='Directly input prompt text'
)
@click.option(
    '-f', '--file',
    type=click.File('r'),
    help='Read prompt from a file'
)
@click.option(
    '-i', '--interactive',
    is_flag=True,
    help='Start interactive mode'
)
@click.option(
    '--no-menu',
    is_flag=True,
    help='Display results only without menu selection'
)
def main(prompt, file, interactive, no_menu):
    """
    🚀 Prompt Optimizer - AI prompt optimizer
    
    Optimizes prompts for token efficiency.
    Makes prompts more concise before sending to ChatGPT, Claude, and other AI models.
    """
    cli = PromptOptimizerCLI()

    try:
        if file:
            # Read from file
            prompt_text = file.read().strip()
            cli.process_prompt(prompt_text, show_menu=not no_menu)

        elif prompt:
            # Direct prompt input
            cli.process_prompt(prompt, show_menu=not no_menu)

        elif interactive or (not prompt and not file):
            # Interactive mode (default if no args)
            cli.interactive_mode()

    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
